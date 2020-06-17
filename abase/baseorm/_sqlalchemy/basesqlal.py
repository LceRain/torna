# _*_ coding: utf8 _*_
from sqlalchemy import create_engine    # 创建引擎对象
from sqlalchemy.orm import sessionmaker  # 创建数据库连接会话
from sqlalchemy.ext.declarative import declarative_base  # 基础模块
from sqlalchemy import Column, String, Integer

import pymysql

from tornas import settings

pymysql.install_as_MySQLdb()


engin = create_engine(settings.DATABASES['default'], echo=False)
# '数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
Session = sessionmaker(bind=engin)
session = Session()


Base = declarative_base(bind=engin)






# if __name__ == '__main__':
#
#     class Person(Base):
#         __tablename__ = 'person'
#         id = Column(Integer, primary_key=True)
#         name = Column(String(30))
#         age = Column(Integer)
#
#         def __str__(self):
#             return '<Person id=' + str(self.id) + ', name=' + str(self.name) + ', age' + str(self.age) + '>'
#
#
#
#     # Base.metadata.create_all()   # 将所有salalchemy管理的对象同步到数据库中产生对应的数据表
#
#     # 增删改
#
#     # p = Person(name='jerry', age=12)  # 临时状态，程序创建对象，临时对象   特点：程序中有数据，缓存中无数据，数据库中无数据
#     #
#     # session.add(p)  # 缓存状态(托管状态)：只是存在于连接会话缓存中，数据库中并没有相关数据，缓存对象  特点：程序中有数据，缓存中有数据，数据库中无数据
#     # session.commit()  # 持久状态(持久persistent状态)：对象在程序中存在，在数据库中有对应的记录  特点：程序中有数据{id}， 缓存中有数据， 数据库中有数据
#     #
#     # '''
#     # 修改操作:
#     # 特点：一旦对缓存状态的对象进行修改，此时缓存对象和数据库中的数据不一致~~就会形成脏数据，脏数据并不是不可取的，更新操作就是将这样的数据从缓存同步到数据库(commit)
#     # '''
#     # p.name = 'shuke'
#     # print(session.dirty.pop())  # 弹出一个
#     # session.commit()
#     #
#     # session.delete(p)  # 直接删除一个缓存的数据[脏数据]，通过commit()提交到数据库
#     # session.commit()
#
#     # 注意删除的只能是持久对象
#     #p2 = Person(id=1)
#     #session.delete(p2)
#     # 抛出异常~不能删除，因为p2不是持久对象is not persisted
#
#     #  # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
#     # 查询  得到的都是<class 'sqlalchemy.orm.query.Query'> 可以加.all()获得查询的所有数据
#     # 1、全表查询
#     # 1.1. 直接调用query，就相当于默认调用了all()进行了全表查询
#     person_list = session.query(Person)   # 返回<class 'sqlalchemy.orm.query.Query'>
#     print(person_list, type(person_list))
#     # 1.2. 直接通过all()函数指定进行全表查询
#     person_list = session.query(Person).all()   # 返回列表对象，列表里都是Person对象
#     print(person_list, type(person_list))
#
#     # 2、排序查询
#     # 2.1. 通过 类型.属性 指定按照什么属性进行默认顺序排序
#     person_list = session.query(Person).order_by(Person.id)
#     print(person_list, type(person_list))
#     # 2.2. 通过 -类型.属性 指定按照什么属性进行倒序排序
#     person_list = session.query(Person).order_by(-Person.id)
#     print(person_list, type(person_list))
#     # 2.3. 通过 类型.属性,类型.属性~指定多列，表示按照多列进行排序，
#     # 如果第一列数据相同，按照第二列进行排序，以此类推。
#     person_list = session.query(Person).order_by(Person.name, Person.age)
#     print(person_list, type(person_list))
#
#     # 3、指定查询
#     # 模拟sql语句中的指定列查询 select p.name from person p;
#     # 生成的sql语句：SELECT persons.name AS persons_name FROM persons
#     #只查找person 的name
#     person_list = session.query(Person.name)
#     print(person_list)
#
#
#     # 5、切片查询
#     #一般使用在数据分页查询等这样的业务中，切片查询
#     # 由于sqlalchemy查询的结果就是一个like list的存在，所以直接用Python的切片即可。
#     # 如果网页页面中的数据~需要分页展示，每页两条记录
#     #~start = (pageno-1)*pagecount, end: start+pagecount
#     person_list = session.query(Person).all()[:2] # 第一页数据  [0, 2]
#     print(person_list,type(person_list))
#     person_list = session.query(Person).all()[2:4] # 第二页数据 [2, 4]
#     print(person_list, type(person_list))
#
#     # 6、filter()[常用]条件查询
#     # 6.1. 等值查询 | 非等值查询
#     person_list = session.query(Person).filter(Person.name!="tom")
#     print(person_list, type(person_list))
#     person_list = session.query(Person).filter(Person.name=="tom")
#     print(person_list, type(person_list))
#     # 6.2. 模糊查询
#     #name 里包含 e 字母的用户
#     person_list = session.query(Person).filter(Person.name.like('%e%'))
#     print(person_list, type(person_list))
#     # 6.3. 范围查询：in 和 not in
#     # in   查询名字叫Tom 和Jerry 的所有人
#     person_list = session.query(Person).filter(Person.name.in_(['tom', 'jerry']))
#     print(person_list, type(person_list))
#     # not in   查询名字不叫Tom 和Jerry 的所有人
#     person_list = session.query(Person).filter(Person.name.in_(['tom', 'jerry']))
#     print(person_list, type(person_list))
#     # 6.4. 空值查询 is null / is not null
#     # 空值
#     person_list = session.query(Person).filter(Person.name == None) # 常用~但是不是规范
#     print(person_list, type(person_list))
#     person_list= session.query(Person).filter(Person.name.is_(None)) # 不太常用~pep8编码规范推荐
#     print(person_list, type(person_list))
#     # 非空值
#     person_list = session.query(Person).filter(Person.name != None)
#     print(person_list, type(person_list))
#     person_list = session.query(Person).filter(Person.name.isnot(None))
#     print(person_list, type(person_list))
#     # 6.5. 并且条件 和 或者条件 查询
#     # 并且条件的查询，有三种实现模式
#     # 第一种：多个filter
#     person_list = session.query(Person).filter(Person.name=="tom").filter(Person.age==12)
#     print(person_list, type(person_list))
#     # 第二种：一个filter，多个条件
#     person_list = session.query(Person).filter(Person.name=="tom", Person.age==12)
#     print(person_list, type(person_list))
#     # 第三种：规范并且条件查询方式：通过and_()函数收集条件
#     from sqlalchemy import and_
#     person_list = session.query(Person).filter(and_(Person.name == 'tom', Person.age==12))
#     print(person_list, type(person_list))
#     # 或者查询：or 查询，通过or_()函数进行查询
#     from sqlalchemy import or_
#     person_list = session.query(Person).filter(or_(Person.name == 'tom', Person.name=='jerry'))
#     print(person_list, type(person_list))
#     # 6.6. 定制化SQL语句查询
#
#     # 导入模块
#     from sqlalchemy import text
#
#     person_list = session.query(Person)\
#       .from_statement(text("select p.id, p.name, p.age from persons p where name=:myname"))\
#       .params(myname="tom").all()






