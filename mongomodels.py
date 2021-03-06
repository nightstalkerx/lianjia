import datetime

from conf import config
from log import error, info, success, warning
from mongoengine import *

connect(host=config.mongo_uri)


class oldHouse(Document):
    hid = StringField(max_length=64, require=True)
    url = URLField()
    city = StringField()
    intime = DateTimeField(default=datetime.datetime.utcnow)
    img_main = URLField()
    title = StringField()
    tags = ListField()
    addrtype = StringField()
    roomtype = StringField()
    area = FloatField()
    decoration = StringField()
    direction = ListField()
    price_sum = FloatField()
    price_avg = FloatField()
    hangtag = DateTimeField()
    levelType = StringField(default="低楼层")
    levelNum = IntField(default=1)
    style = StringField()
    elevator = BooleanField(default=False)
    decade = StringField()
    useage = StringField()
    ownership = StringField()
    community = StringField()
    location = StringField()
    agents = ListField()
    address = StringField()
    details = StringField()
    day7 = IntField(default=0)
    day30 = IntField(default=0)
    attention = IntField(default=0)


class agent(Document):
    uid = StringField(require=True)
    intime = DateTimeField(default=datetime.datetime.utcnow)
    name = StringField(max_length=6)
    img = URLField()
    types = StringField()
    certification = ListField()
    worktime = StringField()
    historytransaction = IntField()
    avgtransactiontime = FloatField()
    day30service = IntField()
    tags = ListField()
    reviews = DictField()
    message = DictField()
    tel = IntField()


class newHouse(Document):
    hid = StringField(max_length=64, require=True)
    city = StringField()
    intime = DateTimeField(default=datetime.datetime.utcnow)
    url = URLField()
    title = StringField()
    addrtype = StringField()
    roomtype = StringField()
    tags = ListField()
    price_sum = StringField()
    price_bunch = StringField()
    area = StringField()
    hangtag = DateTimeField()
    address = StringField()
    location = StringField()
    more = StringField()
    huxings = ListField()
    tel = StringField()


class chuzuHouse(Document):
    hid = StringField()
    city = StringField()
    intime = DateTimeField(default=datetime.datetime.utcnow)
    url = URLField()
    title = StringField()
    img_main = URLField()
    tags = ListField()
    price = IntField()
    description = ListField()
    details = StringField()
    area_type = StringField()
    area = StringField()
    location = StringField()
    hangtag = StringField()
    checkin = StringField()
    view = StringField()
    levelType = StringField()
    levelNum = IntField()
    elevator = BooleanField()
    parking = BooleanField()
    water = BooleanField()
    power = BooleanField()
    gas = BooleanField()
    heater = BooleanField()
