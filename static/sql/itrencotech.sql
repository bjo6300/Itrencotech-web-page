CREATE TABLE `member` (
	`id`	varchar(20)	NOT NULL,
	`name`	varchar(50)	NOT NULL,
	`passwd`	varchar(30)	NOT NULL,
	`phone_num`	char(13)	NOT NULL,
	`email`	varchar(30)	NOT NULL,
	`company_name`	varchar(30)	NOT NULL,
	`company_num`	char(13)	NOT NULL,
	`company_address`	varchar(100)	NOT NULL
);

CREATE TABLE `portfolio` (
	`board_index`	int	NOT NULL,
	`category_index`	int	NOT NULL,
	`portfolio_img`	varchar(100)	NOT NULL
);

CREATE TABLE `review` (
	`board_index`	int	NOT NULL,
	`rating`	double	NOT NULL,
	`date`	date	NOT NULL,
	`content`	varchar(100)	NOT NULL,
	`review_img`	varchar(100)	NOT NULL,
	`Field2`	VARCHAR(255)	NOT NULL,
	`category_index`	int	NOT NULL,
	`id`	varchar(20)	NOT NULL
);

CREATE TABLE `category` (
	`category_index`	int	NOT NULL,
	`category_main`	varchar(50)	NOT NULL,
	`category_sub`	varchar(50)	NOT NULL
);

CREATE TABLE `order` (
	`order_num`	unsigned int	NOT NULL,
	`business_num`	varchar(255)	NOT NULL,
	`name`	varchar(30)	NOT NULL,
	`email`	varchar(50)	NOT NULL,
	`phone_num`	char(13)	NOT NULL,
	`title`	varchar(30)	NOT NULL,
	`description`	varchar(255)	NOT NULL,
	`material`	varchar(30)	NOT NULL,
	`quantity`	int	NOT NULL	DEFAULT "1",
	`size`	varchar(255)	NOT NULL,
	`path`	varchar(255)	NOT NULL,
	`etc`	varchar(255)	NULL,
	`state`	varchar(10)	NOT NULL	DEFAULT "접수 완료",
	`id`	varchar(20)	NOT NULL,
	`category_index`	int	NOT NULL
);

ALTER TABLE `member` ADD CONSTRAINT `PK_MEMBER` PRIMARY KEY (
	`id`
);

ALTER TABLE `portfolio` ADD CONSTRAINT `PK_PORTFOLIO` PRIMARY KEY (
	`board_index`,
	`category_index`
);

ALTER TABLE `review` ADD CONSTRAINT `PK_REVIEW` PRIMARY KEY (
	`board_index`
);

ALTER TABLE `category` ADD CONSTRAINT `PK_CATEGORY` PRIMARY KEY (
	`category_index`
);

ALTER TABLE `order` ADD CONSTRAINT `PK_ORDER` PRIMARY KEY (
	`order_num`
);

ALTER TABLE `portfolio` ADD CONSTRAINT `FK_category_TO_portfolio_1` FOREIGN KEY (
	`category_index`
)
REFERENCES `category` (
	`category_index`
);

ALTER TABLE `review` ADD CONSTRAINT `FK_category_TO_review_1` FOREIGN KEY (
	`category_index`
)
REFERENCES `category` (
	`category_index`
);

ALTER TABLE `review` ADD CONSTRAINT `FK_member_TO_review_1` FOREIGN KEY (
	`id`
)
REFERENCES `member` (
	`id`
);

ALTER TABLE `order` ADD CONSTRAINT `FK_member_TO_order_1` FOREIGN KEY (
	`id`
)
REFERENCES `member` (
	`id`
);

ALTER TABLE `order` ADD CONSTRAINT `FK_category_TO_order_1` FOREIGN KEY (
	`category_index`
)
REFERENCES `category` (
	`category_index`
);

