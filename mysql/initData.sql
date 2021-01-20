
drop table if exists trade;
create table trade
(
    id        bigint auto_increment primary key,
    from_type varchar(20) not null,
    deal_id   bigint null,
    deal_time bigint null,
    price     decimal(20, 10) null,
    amount    decimal(20, 10) null,
    direction varchar(10) null
);