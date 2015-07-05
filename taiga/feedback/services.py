# coding: utf-8
# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
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

from django.conf import settings

from djmail.template_mail import MagicMailBuilder, InlineCSSTemplateMail


def send_feedback(feedback_entry, extra, reply_to=[]):
    support_email = settings.FEEDBACK_EMAIL

    if support_email:
        reply_to.append(support_email)

        ctx = {
            "feedback_entry": feedback_entry,
            "extra": extra
        }

        mbuilder = MagicMailBuilder(template_mail_cls=InlineCSSTemplateMail)
        email = mbuilder.feedback_notification(support_email, ctx)
        email.extra_headers["Reply-To"] = ", ".join(reply_to)
        email.send()
