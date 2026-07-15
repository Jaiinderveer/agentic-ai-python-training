from session13 import DBHelper
def main():
    db = DBHelper()
    db.select_collection()
    # condition = {'email':'jai@gmail.com'}
    
    # Assignment: Explore Operators in MongoDB eg: age is greater than 12 and less than 20
    
    # db.retrieve(condition)
    # condition = {'email':'fionna@example.com'}
    # document_to_update = {
    #     'name': 'Fionna Jackson',
    #     'phone': '+91 99119 99119'
    # }
    # db.update(condition,document_to_update)
    condition = {'email':'fionna@example.com'}
    db.delete(condition)
    
if __name__ == '__main__':
    main()