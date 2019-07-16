# # # This is an auto-generated Django model module.
# # # You'll have to do the following manually to clean this up:
# # #   * Rearrange models' order
# # #   * Make sure each model has one field with primary_key=True
# # #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# # #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # # Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Article(models.Model):
    a_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=511)
    pub_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'article'



class ArticlePhoto(models.Model):
    ap_id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, models.PROTECT, blank=True, null=True)
    path = models.CharField(max_length=128)

    class Meta:
        # managed = False
        db_table = 'ar_photo'


# class Cat(models.Model):
#     cat_id = models.AutoField(primary_key=True)
#     # catvari = models.OneToOneField('CatVari', models.PROTECT, db_column = 'cat_vari_id')
#     ch_name = models.CharField(max_length=128, blank=True, null=True)
#     en_name = models.CharField(max_length=128, blank=True, null=True)
#     alias = models.CharField(max_length=128, blank=True, null=True)
#     shape = models.CharField(max_length=128, blank=True, null=True)
#     origin = models.CharField(max_length=128, blank=True, null=True)
#     price = models.IntegerField(blank=True, null=True)
#     cat_like = models.CharField(max_length=128, blank=True, null=True)
#     cat_character = models.CharField(max_length=128, blank=True, null=True)
#     sti_degree = models.IntegerField(blank=True, null=True)
#     bar_degree = models.IntegerField(blank=True, null=True)
#     hair_loss_degree = models.IntegerField(blank=True, null=True)
#     fri_degree = models.IntegerField(blank=True, null=True)
#     ani_fri_degree = models.IntegerField(blank=True, null=True)
#     trainability = models.IntegerField(blank=True, null=True)
#     city_degree = models.IntegerField(blank=True, null=True)
#     feature = models.CharField(max_length=128, blank=True, null=True)
#     attention = models.CharField(max_length=128, blank=True, null=True)
#     nurturing_knowledge = models.CharField(max_length=128, blank=True, null=True)
#
#     class Meta:
#         # managed = False
#         db_table = 'cat'


class CatDisease(models.Model):
    cat_dis_id = models.AutoField(primary_key=True)
    dis_name = models.CharField(max_length=128, null=True)
    performace = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'cat_disease'


class CatVari(models.Model):
    cati_id = models.AutoField(primary_key=True)
    cat_vari_name = models.CharField(max_length=64, blank=True, null=True)
    cat_vari_img = models.CharField(max_length=128, blank=True, null=True)
    # ch_name = models.CharField(max_length=128, blank=True, null=True)
    alias = models.CharField(max_length=32, blank=True, null=True)
    en_name = models.CharField(max_length=32, blank=True, null=True)
    weight = models.CharField(max_length=32,blank=True, null=True)
    shape = models.CharField(max_length=32, blank=True, null=True)
    origin = models.CharField(max_length=32, blank=True, null=True)
    price = models.CharField(max_length=32,blank=True, null=True)
    cat_habit = models.CharField(max_length=2560, blank=True, null=True)
    # cat_character = models.CharField(max_length=2560, blank=True, null=True)
    sti_degree = models.IntegerField(blank=True, null=True)
    bar_degree = models.IntegerField(blank=True, null=True)
    hair_loss_degree = models.IntegerField(blank=True, null=True)
    fri_degree = models.IntegerField(blank=True, null=True)
    ani_fri_degree = models.IntegerField(blank=True, null=True)
    trainability = models.IntegerField(blank=True, null=True)
    city_degree = models.IntegerField(blank=True, null=True)
    feature = models.CharField(max_length=2560, blank=True, null=True)
    attention = models.CharField(max_length=2560, blank=True, null=True)
    nurturing_knowledge = models.CharField(max_length=2560, blank=True, null=True)


    class Meta:
        # managed = False
        db_table = 'cat_vari'


class CatPhoto(models.Model):
    cp_id = models.AutoField(primary_key=True)
    catvari = models.ForeignKey(CatVari, models.PROTECT, blank=True, null=True)
    path = models.CharField(max_length=128)

    class Meta:
        # managed = False
        db_table = 'cat_photo'




class DynamicTag(models.Model):
    dt_id = models.AutoField(primary_key=True)
    dynamic = models.ForeignKey('Dynamic', models.PROTECT, related_name='dy1')
    tag = models.ForeignKey('Tag', models.PROTECT, db_column='tag_id',related_name='ta')

    class Meta:
        # managed = False
        db_table = 'd_tag'


class DogDiseaseMedicine(models.Model):
    ddm_id = models.AutoField(primary_key=True)
    medicine = models.ForeignKey('Medicine', models.PROTECT, related_name='d_med')
    dog_disease = models.ForeignKey('DogDisease', models.PROTECT, related_name='m_d')

    class Meta:
        # managed = False
        db_table = 'dm_dis'

#
# class Dog(models.Model):
#     dog_id = models.AutoField(primary_key=True)
#     ch_name = models.CharField(max_length=128)
#     en_name = models.CharField(max_length=128)
#     origin = models.CharField(max_length=128, blank=True, null=True)
#     shape = models.CharField(max_length=128, blank=True, null=True)
#     price = models.IntegerField(blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#     sti_degree = models.IntegerField(blank=True, null=True)
#     bar_degree = models.IntegerField(blank=True, null=True)
#     hairloss_degree = models.IntegerField(blank=True, null=True)
#     fri_degree = models.IntegerField(blank=True, null=True)
#     stranger_frii_degree = models.IntegerField(blank=True, null=True)
#     compliance = models.IntegerField(blank=True, null=True)
#     home_degree = models.IntegerField(blank=True, null=True)
#     dog_vari = models.OneToOneField('DogVari', on_delete=models.PROTECT, db_column='dog_vari_id')
#     feature = models.CharField(max_length=128, blank=True, null=True)
#     attention = models.CharField(max_length=128, blank=True, null=True)
#     nurturing_knowledge = models.CharField(max_length=511, blank=True, null=True)
#
#     class Meta:
#         # managed = False
#         db_table = 'dog'


class DogDisease(models.Model):
    dog_dis_id = models.AutoField(primary_key=True)
    dis_name = models.CharField(max_length=128)
    dis_code = models.CharField(max_length=128)
    performace = models.CharField(max_length=128)

    class Meta:
        # managed = False
        db_table = 'dog_dissease'


class DogVari(models.Model):
    dog_vari_id = models.AutoField(primary_key=True)
    dog_vari_name = models.CharField(max_length=20, blank=True, null=True)
    dog_vari_img = models.CharField(max_length=128, blank=True, null=True)
    # ch_name = models.CharField(max_length=128)
    alias = models.CharField(max_length=32, blank=True, null=True)
    en_name = models.CharField(max_length=32, null=True)
    origin = models.CharField(max_length=32, blank=True, null=True)
    shape = models.CharField(max_length=20, blank=True, null=True)
    price = models.CharField(max_length=32,blank=True, null=True)
    weight = models.CharField(max_length=32,blank=True, null=True)
    sti_degree = models.IntegerField(blank=True, null=True)
    bar_degree = models.IntegerField(blank=True, null=True)
    hairloss_degree = models.IntegerField(blank=True, null=True)
    fri_degree = models.IntegerField(blank=True, null=True)
    stranger_frii_degree = models.IntegerField(blank=True, null=True)
    compliance = models.IntegerField(blank=True, null=True)
    home_degree = models.IntegerField(blank=True, null=True)
    # dog_vari = models.OneToOneField('DogVari', on_delete=models.PROTECT, db_column='dog_vari_id')
    feature = models.CharField(max_length=5120, blank=True, null=True)
    attention = models.CharField(max_length=5120, blank=True, null=True)
    nurturing_knowledge = models.CharField(max_length=5120, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'dog_vari'


class DogPhoto(models.Model):
    dp_id = models.AutoField(primary_key=True)
    dogvari = models.ForeignKey(DogVari, models.PROTECT, blank=True, null=True, db_column='dogvari')
    dp_path = models.CharField(max_length=128)

    class Meta:
        # managed = False
        db_table = 'dog_photo'


class Dynamic(models.Model):
    d_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', models.PROTECT, blank=True, null=True)
    text_content = models.CharField(max_length=512)
    pub_time = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    g_counts = models.IntegerField(blank=True, null=True)
    is_public = models.BooleanField(default=1)
    tags = models.ManyToManyField(to='tag', through=DynamicTag)
    status = models.BooleanField(default=1)

    class Meta:
        # managed = False
        db_table = 'dynamic'





class Medicine(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_name = models.CharField(max_length=128, blank=True, null=True)
    m_function = models.CharField(max_length=128, blank=True, null=True)
    m_explain = models.CharField(max_length=128, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    addr = models.CharField(max_length=128, blank=True, null=True)
    manufacturer = models.CharField(max_length=128, blank=True, null=True)
    price = models.CharField(max_length=128, blank=True, null=True)
    qua_date = models.DateField(blank=True, null=True)
    dog_disease = models.ManyToManyField(to=DogDisease, through=DogDiseaseMedicine)
    cat_disease = models.ManyToManyField(to=CatDisease, through='MedicineDis')

    class Meta:
        # managed = False
        db_table = 'medicine'


class MedicineDis(models.Model):
    id = models.AutoField(primary_key=True)
    medicine = models.ForeignKey(Medicine, models.PROTECT, related_name='c_med')
    cat_disease = models.ForeignKey(CatDisease, models.PROTECT,related_name='m_c')

    class Meta:
        # managed = False
        db_table = 'm_dis'


class Permission(models.Model):
    p_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=128)
    p_code = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'pemission'



class PetDoctor(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=128)
    sex = models.IntegerField()
    years = models.IntegerField()
    area = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'petdoctor'


class Photo(models.Model):
    p_id = models.AutoField(primary_key=True)
    d = models.ForeignKey(Dynamic, models.PROTECT, blank=True, null=True)
    p_path = models.CharField(max_length=128)
    pub_time = models.DateTimeField(blank=True, null=True, auto_now_add=True)

    class Meta:
        # managed = False
        db_table = 'photo'



class Role(models.Model):
    r_id = models.IntegerField(primary_key=True)
    r_name = models.CharField(max_length=128, blank=True, null=True)
    r_code = models.CharField(max_length=128, blank=True, null=True)
    permissions = models.ManyToManyField(to=Permission, through='RolePermission')

    class Meta:
        # managed = False
        db_table = 'role'


class RolePermission(models.Model):
    rp_id = models.AutoField(primary_key=True)
    pemission = models.ForeignKey(Permission, models.PROTECT, related_name='per')
    role = models.ForeignKey(Role, models.PROTECT,related_name='p_r')

    class Meta:
        # managed = False
        db_table = 'r_p'


class Tag(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_content = models.CharField(max_length=128)

    class Meta:
        # managed = False
        db_table = 'tag'




# class UserTag(models.Model):
#     ut_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey('User', models.PROTECT, related_name='u_t')
#     tag = models.ForeignKey(Tag, models.PROTECT, db_column='id',related_name='tags')

    # class Meta:
    #     # managed = False
    #     db_table = 'u_tag'


class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=128)
    birthday = models.DateTimeField(blank=True, null=True)
    u_password = models.CharField(max_length=128)
    addres = models.CharField(max_length=128, blank=True, null=True)
    tel = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    icon = models.CharField(max_length=128, blank=True, null=True)
    sign = models.CharField(max_length=128, blank=True, null=True)
    sex = models.IntegerField(default=1)
    realname = models.CharField(max_length=128, blank=True, null=True)
    reg_date = models.DateTimeField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    lastvisit = models.DateTimeField(blank=True, null=True)
    # flowing = models.ManyToManyField(to='self', through='UserFlowing')
    # flower = models.ManyToManyField(to='self', through='UserFlower')
    # tag = models.ManyToManyField(to=Tag, through=UserTag)
    roles = models.ManyToManyField(to=Role, through='UserRole')

    def __str__(self):
        return self.u_name


    class Meta:
        # managed = False
        db_table = 'user'


class UserRole(models.Model):
    ur_id = models.AutoField(primary_key=True)
    role = models.ForeignKey(Role, models.PROTECT, related_name='roles')
    user = models.ForeignKey(User, models.PROTECT,related_name='u_r')

    class Meta:
        # managed = False
        db_table = 'u_r'



class PetInfo(models.Model):
    p_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.PROTECT, blank=True, null=True)
    p_name = models.CharField(max_length=128)
    p_type = models.IntegerField()
    p_birthday = models.DateTimeField(blank=True, null=True)
    verities = models.CharField(max_length=128)

    class Meta:
        # managed = False
        db_table = 'pet_info'


class Collection(models.Model):
    col_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.PROTECT, blank=True, null=True)
    col_time = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    dynamic = models.ForeignKey(Dynamic, models.PROTECT, blank=True, null=True)
    status = models.BooleanField(default=1)

    class Meta:
        # managed = False
        db_table = 'collection'


# class DynamicCollection(models.Model):
#     dc_id = models.AutoField(primary_key=True)
#     dynamic = models.ForeignKey(Dynamic, models.PROTECT, related_name='dy0')
#     collection = models.ForeignKey(Collection, models.PROTECT,related_name='col')
#
#     class Meta:
#         # managed = False
#         db_table = 'd_collection'


class Comment(models.Model):
    c_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.PROTECT, blank=True, null=True)
    dynamic = models.ForeignKey(Dynamic, models.PROTECT, blank=True, null=True)
    com_c = models.ForeignKey('self', models.PROTECT, blank=True, null=True)
    c_content = models.CharField(max_length=511)
    c_time = models.DateTimeField(blank=True, null=True, auto_now=True)
    c_counts = models.IntegerField(blank=True, null=True)
    status = models.BooleanField(default=1)

    class Meta:
        # managed = False
        db_table = 'comment'



class UserFollower(models.Model):
    u_follower_id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    follower_id = models.IntegerField()
    status = models.BooleanField()

    class Meta:
        # managed = False
        db_table = 'user_flower'


class UserFlowing(models.Model):
    u_following_id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    following_id = models.IntegerField()
    status = models.BooleanField(default=1)


    class Meta:
        # managed = False
        db_table = 'user_flowing'

class Nice(models.Model):
    n_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.PROTECT, related_name='nice_u')
    dynamic = models.ForeignKey(Dynamic, models.PROTECT, related_name='nice_d')
    comment = models.ForeignKey(Comment, models.PROTECT, related_name='nice_c')
    status = models.BooleanField(default=1)


    class Meta:
        # managed = False
        db_table = 'tb_nice'


class UserToken(models.Model):
    """用户身份令牌"""
    tokenid = models.AutoField(primary_key=True)
    token = models.CharField(max_length=511)
    user = models.OneToOneField(to=User, on_delete=models.PROTECT, db_column='userid')

    class Meta:
        db_table = 'tb_user_token'


class CatArticle(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=128)
    article_pic = models.CharField(max_length=128)
    article_content = models.CharField(max_length=12800)

    class Meta:
        db_table = 'cat_article'

class DogArticle(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=128)
    article_pic = models.CharField(max_length=128)
    article_content = models.CharField(max_length=12800)

    class Meta:
        db_table = 'dog_article'
