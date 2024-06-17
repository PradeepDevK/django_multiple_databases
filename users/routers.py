class UsersRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'users_db'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'users':
            return 'users_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'users' or obj2._meta.app_label == 'users':
            return True
        return None
    
    # Exclude the 'User' model from migration in the default database
    def allow_migrate(self, db, app_lable, model_name=None, **hints):
        if db == 'default' and model_name == 'User':
            return False
        return True
            