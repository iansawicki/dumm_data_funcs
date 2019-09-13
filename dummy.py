read_it = lambda x: pd.read_csv(x)
hash_it = lambda x: hashlib.sha256(x.encode('utf-8')).hexdigest()
hash_it_sha1 = lambda x: hashlib.sha3_256(x.encode('utf-8')).hexdigest()
join_it = lambda a,b: a.merge(b,how="left",on="Id")
def rand_name(x):
    return names.get_full_name()

def first_name(x):
    return names.get_first_name()

def last_name(x):
    return names.get_last_name()

def random_null(c):
    thresh = 1 #1 percent of data will be made null
    val = np.random.random_integers(200)
    if val == thresh:
        return(None)
    else:
        return(c)
    
def random_int(c):
    return(np.random.randint(5)+1)

def random_tier(c):
    tiers = ["Standard","Preferred","Premier"]
    return(tiers[np.random.randint(2)])

def random_stage(c):
    tiers = ["Registered","Downloaded App","Opened App","Login Attempted - Failed","Login Tries Exceeded - Locked Out","App Tour Completed","Viewed Balance"]
    return(tiers[np.random.randint(len(tiers))])

def random_bool(c):
    return([False,True][np.random.randint(2)])


def convert_time(c):
    return(dt.strptime(c,"%m/%d/%y"))

def add_days(c):
    if isinstance(c,str):
        return(convert_time(c)+td(days=np.random.randint(60)))
    if isinstance(c,dt):
        return(c+td(days=np.random.randint(60)))
    return

def subtract_days(c):
    if isinstance(c,str):
        return(convert_time(c)-td(days=np.random.randint(730)))
    if isinstance(c,dt):
        return(c-td(days=np.random.randint(730)))
    return
    
def add_days_2(c):
    if isinstance(c,str):
        return(convert_time(c)+td(days=np.random.randint(30)))
    if isinstance(c,dt):
        return(c+td(days=np.random.randint(30)))
    return




