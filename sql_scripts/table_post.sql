use campus_couple;
drop table if exists post;
create table post(
	post_id tinyint primary key auto_increment,
<<<<<<< HEAD
	add_time TIMEdSTAMP DEFAULT now() ,
=======
	add_time TIMESTAMP DEFAULT now() ,
>>>>>>> b478ea35ee4fd0d81a176d47911ab7d4e8e29c84
	user_id tinyint not null,
	content varchar(140)
)engine=InnoDB default charset=utf8;

drop table if exists post_img;
create table post_img(
	post_id int ,
	img_url varchar(100)
)engine=InnoDB default charset=utf8;

drop table if exists favor;
create table favor(
	post_id int ,
	user_id int
)engine=InnoDB default charset=utf8;

drop table if exists comments;
create table comments(
	post_id int not null,
	user_id int not NULL ,#评论者的id
	comment_id int PRIMARY KEY AUTO_INCREMENT,
	commented_id int, #被评论的评论者id
	content varchar(60) ,
	add_time TIMESTAMP
)engine=InnoDB default charset=utf8;

drop table if exists follow;
create table follow(
	user_id int not null,
	followed_id int not null
)engine=InnoDB default charset=utf8;

