from Config import Configuration

def CloseCard(ID_num):
    db = Configuration()
    db.connect()

    # 加个贷款判断

    
    return db.delete('cards',{'cardid':ID_num})
    
    
