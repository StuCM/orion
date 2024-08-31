from tortoise import fields, models
import bcrypt

class Users(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    password = fields.CharField(max_length=128, null=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    async def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('$2b$'):
            self.password = bcrypt.hashSync(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        await super().save(*args, **kwargs)