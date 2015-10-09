from flask.ext.wtf import Form
from wtforms import FloatField, IntegerField, SelectField, StringField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms_alchemy import model_form_factory
from tabs.database import Users

BaseModelForm = model_form_factory(Form)

class NewsForm(Form):

    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Body', validators=[DataRequired()])
    user_id = StringField('User Id', validators=[DataRequired()])
    

class UpdateForm(Form):

    title = StringField('Title', validators=[DataRequired()])
    body = StringField('Body', validators=[DataRequired()])
    user_id = StringField('User Id', validators=[DataRequired()])
    

class UserForm(Form):
    # class Meta:
    #     model = Users
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])


class ProjectForm(Form):

    name = StringField('Name', validators=[DataRequired()])
    user_id = StringField('User Id', validators=[DataRequired()])


class SampleForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    project = StringField('Project', validators=[DataRequired()])


class SequencingForm(Form):
    name = SelectField('Type', 
            choices=[('atac','ATACSeq'), 
                ('chip', 'ChipSeq'),
                ('dnase', 'DNASeq'),
                ('rna', 'RNASeq'),],
            validators=[DataRequired()])
    preparation = StringField('Preparation', validators=[DataRequired()])


class PreparationForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    antibody = StringField('Antibody', validators=[DataRequired()])
    cell_line = StringField('Cell Line', validators=[DataRequired()])
    bioanalyzer_shearing = StringField('Bioanalyzer Shearing', validators=[DataRequired()])
    library_yield = FloatField('Library Yield', validators=[DataRequired()])
    adaptor = StringField('Adaptor', validators=[DataRequired()])
    bioanalyzer_library = StringField('Bioanalyzer Library', validators=[DataRequired()])
    amount_submitted = IntegerField('Amount Submitted', validators=[DataRequired()])
    concentration = FloatField('Concentration', validators=[DataRequired()])
    fedex_tracking_number = StringField('Fedex Tracking Number')
    comments = TextAreaField('Comments')
    sample = StringField('Sample', validators=[DataRequired()])

class ProcessingForm(Form):
    name = StringField('Name', validators=[DataRequired()])
    host = StringField('Host', validators=[DataRequired()])
    cmd = StringField('Command', validators=[DataRequired()])
    output_dir = StringField('Output Directory', validators=[DataRequired()])
    sequencing = StringField('Sequencing', validators=[DataRequired()])
    
