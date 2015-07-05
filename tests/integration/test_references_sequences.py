# coding: utf-8
# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014 Anler Hernández <hello@anler.me>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pytest

from .. import factories


@pytest.fixture
def seq():
    from taiga.projects.references import sequences as seq
    return seq


@pytest.fixture
def refmodels():
    from taiga.projects.references import models
    return models


@pytest.mark.django_db
def test_sequences(seq):
    seqname = "foo"
    assert not seq.exists(seqname)

    # Create and check values
    seq.create(seqname)
    assert seq.exists(seqname)
    assert seq.next_value(seqname) == 1
    assert seq.next_value(seqname) == 2

    # Delete sequence
    seq.delete(seqname)
    assert not seq.exists(seqname)

    # Create new seq with same name
    # after previously deleted it
    seq.create(seqname)
    assert seq.next_value(seqname) == 1

    # Alter sequence
    seq.alter(seqname, 4)
    assert seq.next_value(seqname) == 5

    # Delete after alter
    seq.delete(seqname)
    assert not seq.exists(seqname)


@pytest.mark.django_db
def test_unique_reference_per_project(seq, refmodels):
    project = factories.ProjectFactory.create()
    seqname = refmodels.make_sequence_name(project)

    assert seqname == "references_project{0}".format(project.id)
    assert seq.exists(seqname)

    assert refmodels.make_unique_reference_id(project, create=True) == 1
    assert refmodels.make_unique_reference_id(project, create=True) == 2

    project.delete()
    assert not seq.exists(seqname)


@pytest.mark.django_db
def test_regenerate_us_reference_on_project_change(seq, refmodels):
    project1 = factories.ProjectFactory.create()
    seqname1 = refmodels.make_sequence_name(project1)
    project2 = factories.ProjectFactory.create()
    seqname2 = refmodels.make_sequence_name(project2)

    seq.alter(seqname1, 100)
    seq.alter(seqname2, 200)

    user_story = factories.UserStoryFactory.create(project=project1)
    assert user_story.ref == 101

    user_story.subject = "other"
    user_story.save()
    assert user_story.ref == 101

    user_story.project = project2
    user_story.save()

    assert user_story.ref == 201

@pytest.mark.django_db
def test_regenerate_task_reference_on_project_change(seq, refmodels):
    project1 = factories.ProjectFactory.create()
    seqname1 = refmodels.make_sequence_name(project1)
    project2 = factories.ProjectFactory.create()
    seqname2 = refmodels.make_sequence_name(project2)

    seq.alter(seqname1, 100)
    seq.alter(seqname2, 200)

    task = factories.TaskFactory.create(project=project1)
    assert task.ref == 101

    task.subject = "other"
    task.save()
    assert task.ref == 101

    task.project = project2
    task.save()

    assert task.ref == 201

@pytest.mark.django_db
def test_regenerate_issue_reference_on_project_change(seq, refmodels):
    project1 = factories.ProjectFactory.create()
    seqname1 = refmodels.make_sequence_name(project1)
    project2 = factories.ProjectFactory.create()
    seqname2 = refmodels.make_sequence_name(project2)

    seq.alter(seqname1, 100)
    seq.alter(seqname2, 200)

    issue = factories.IssueFactory.create(project=project1)
    assert issue.ref == 101

    issue.subject = "other"
    issue.save()
    assert issue.ref == 101

    issue.project = project2
    issue.save()

    assert issue.ref == 201
