
``` sql
CREATE DATABASE website;
CREATE TABLE member(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255) NOT NULL, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, follower_count int unsigned NOT NULL DEFAULT 0, time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP);
```
![要求2](./%E8%A6%81%E6%B1%822.png)

``` sql
INSERT INTO member(name ,username, password, follower_count) VALUES('Tony','test','test');
INSERT INTO member(name ,username, password, follower_count) VALUES('Zora','test','test',150);
INSERT INTO member(name ,username, password, follower_count) VALUES('AMY','test','amy',1010);
INSERT INTO member(name ,username, password, follower_count) VALUES('Eva','eva','eva',300);
INSERT INTO member(name ,username, password, follower_count) VALUES('Dog','dog','dog',10);
```
![要求3-1](./%E8%A6%81%E6%B1%823-1.png)
 
 ``` sql
 SELECT * FROM member;
 SELECT * FROM member ORDER BY time DESC;
 ```
![要求3-2~3](./%E8%A6%81%E6%B1%823-2~3.png)

``` sql
SELECT * FROM member ORDER BY time DESC limit 3 offset 1;
SELECT * FROM member WHERE username='test';
SELECT * FROM member WHERE username='test' and password='test';
```
![要求3-4~5](./%E8%A6%81%E6%B1%823-4~5.png)

 
``` sql
UPDATE member SET name='test2' WHERE username='test';
```
![要求3-6](./%E8%A6%81%E6%B1%823-6.png)

``` sql
SELECT COUNT(*) FROM member;
SELECT SUM(follower_count) FROM member;
SELECT AVG(follower_count) FROM member;
```
![要求4](./%E8%A6%81%E6%B1%824.png)

``` sql
CREATE TABLE message(id bigint PRIMARY KEY AUTO_INCREMENT, member_id bigint NOT NULL, content VARCHAR(255) NOT NULL, like_count int unsigned NOT NULL DEFAULT 0, time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP);
INSERT INTO member(member_id ,content, like_count) VALUES(1, '你好', 100);
INSERT INTO member(member_id ,content, like_count) VALUES(2, 'hi', 1200);
INSERT INTO member(member_id ,content, like_count) VALUES(3, 'hello', 2000);
INSERT INTO member(member_id ,content, like_count) VALUES(4, '到此一遊', 200);
INSERT INTO member(member_id ,content, like_count) VALUES(5, '最後一筆', 11000);
```
![要求5](./%E8%A6%81%E6%B1%825.png)

``` sql
SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id;
SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id WHERE username='test';
SELECT AVG(like_count) FROM member INNER JOIN message ON member.id=message.member_id WHERE username='test';
```
![要求5-1~3](./%E8%A6%81%E6%B1%825-1~3.png)

``` sql
ALTER TABLE message ADD FOREIGN KEY(member_id) REFERENCES member(id);
```
![要求5加上外鍵](./%E8%A6%81%E6%B1%825%E5%8A%A0%E4%B8%8A%E5%A4%96%E9%8D%B5.png)
