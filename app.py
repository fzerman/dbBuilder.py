from db_builder.validators.LengthValidator import LengthValidator

c = LengthValidator(value="ahdf-sjodklg",max=50,min=20)

print(c.check())

    