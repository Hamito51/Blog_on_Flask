from wtforms import Form, StringField, TextAreaField 


class PostForm(Form):
    """Structure for PostForm"""
    title = StringField('Title')
    body = TextAreaField('Body')
