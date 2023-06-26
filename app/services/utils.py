def add_arguments(**kwargs):
    def out_wrapper(func):
        def wrapper(*args):
            for item in args:
                if isinstance(item, list):
                    for form in item:
                        for k, v in kwargs.items():
                            form[k] = v
            return func(*args)

        return wrapper

    return out_wrapper

# def create_announcement(announce: dict) -> dict:
#     announce["announce_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     return announce

# 为新用户创建初始信息
# def create_user(user: dict) -> dict:
#     pass  # 输入合法性校验
#     user["create_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     user["last_login_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     user["nickname_text"] = "undefined"
#     user["portrait_url"] = "undefined"
#     user["birthday"] = "2000-1-1"
#     user["gender"] = 1
#     # user["grade"] = ""
#     user["enrollment_date"] = "2000-1-1"
#     user["graduation_date"] = "2000-1-1"
#     user["major_id"] = "2000-1-1"
#     user["is_show_birthday"] = False
#     user["is_show_gender"] = False
#     user["is_show_qq"] = False
#     user["is_show_wechat"] = False
#     user["is_email_show"] = False
#     user["is_major_show"] = False
#     user["is_name_show"] = False
#     user["modify_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     return user
