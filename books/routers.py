class BooksRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'books':
            return 'books_db'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'books':
            return 'books_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'books' or obj2._meta.app_label == 'books':
            return True
        return None
    
    # Exclude the 'Book' model from migration in the default database
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'default' and model_name == 'Book':
            return False
        return True