from caesar import rotate_string
from flask import Flask, request

def buildPage(textarea_content):
    header = "<h2>Web Caesar</h2>"

    rotation_label = "<label>Rotate by:</label>"
    rotation = "<input type='number' name='rotation'/>"
    textarea_label = "<label>Type a message:</label>"
    textarea = "<textarea name='encryption_request'>" + textarea_content + "</textarea>"
    submit = "<input type='submit' />"
    form = "<form method='post'>" + rotation_label + rotation + "<br>" + textarea_label + textarea + "<br>" + submit + "</form>"

    page_content = header + form

    return page_content


    def post(self):
        message = self.request.get("encryption_request")
        rotate_by = int(self.request.get("rotation"))
        encrypted_message = caesar.encrypt(message, rotate_by)
        escaped_message = cgi.escape(encrypted_message)

        content = buildPage(escaped_message)

        self.response.write(content)