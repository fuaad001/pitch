from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    title = StringField('Review title', validators = [Required()])
    review = TextAreaField('Pitch review')
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    category = SelectField('Category', choices=[('', ''), ('pickup lines', 'Pickup Lines'), ('technology', 'Technology Pitches'), ('product', 'Product Pitches'), ('family', 'Family Pitches'), ('jokes', 'Jokes Pitches'), ('motivational', 'Motivational Pitches'), ('educational', 'Educational Pitches')], validators = [Required()])
    title = StringField('Pitch title', validators = [Required()])
    pitch = TextAreaField('Pitch', validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators = [Required()])
    submit = SubmitField('Submit')
