#制作签到user表
CREATE TABLE `signnote`.`shiyongzhe` (
  `user_name` VARCHAR(5) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_unicode_ci' NOT NULL,
  `user_id` CHAR(2) NOT NULL,
  `comment` VARCHAR(30) NULL,
  PRIMARY KEY (`user_id`));

#制作签到记录表
CREATE TABLE `signnote`.`qiandaojilu` (
  `user_id` CHAR(2) NOT NULL,
  `date` DATE NOT NULL,
  `time` TIME NOT NULL,
  `state` CHAR(2) NOT NULL,
  `comment` VARCHAR(30) NULL,
  PRIMARY KEY (`user_id`, `date`, `time`),
  INDEX `fk_note_user_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_note_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `signnote`.`shiyongzhe` (`user_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

# shiyongzhe的插入数据
INSERT INTO `signnote`.`shiyongzhe` (`user_name`, `user_id`, `comment`) VALUES ('佳佳零', '00', '右手食指');
INSERT INTO `signnote`.`shiyongzhe` (`user_name`, `user_id`, `comment`) VALUES ('佳佳绿', '01', '右手中指');
INSERT INTO `signnote`.`shiyongzhe` (`user_name`, `user_id`, `comment`) VALUES ('佳佳饼', '02', '左手食指');
INSERT INTO `signnote`.`shiyongzhe` (`user_name`, `user_id`, `comment`) VALUES ('佳佳针', '03', '左手中指'); 

# 环境变量
echo 'export PWQQ=' >> ~/.bashrc
echo 'export SMTPSERVER=' >> ~/.bashrc
echo 'export ADMINMAIL=' >> ~/.bashrc
echo 'export BOSSMAIL=' >> ~/.bashrc
echo 'export SQLUSER=' >> ~/.bashrc
echo 'export PWSQL=' >> ~/.bashrc
echo 'export SQLDB=' >> ~/.bashrc