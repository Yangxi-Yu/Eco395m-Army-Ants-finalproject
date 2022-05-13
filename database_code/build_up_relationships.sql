--build up relationships among all general tables
--relationship between merge_company_name_industry and merge_jid_cmp
alter table merge_company_name_industry add constraint pk_merge_company_name_industry primary key (company_name);
alter table merge_jid_cmp add constraint fk_merge_jid_cmp_cmp foreign key (company_name) references merge_company_name_industry(company_name);

--relationship between merge_job_des_html and merge_jid_cmp
alter table merge_job_des_html add constraint pk_merge_job_des_html primary key (jid);
alter table merge_jid_cmp add constraint fk_merge_jid_cmp foreign key (jid) references merge_job_des_html (jid);

--relationship between merge_job_des_html and job_basic_information_all
alter table job_basic_information_all add constraint fk_job_basic_information_all foreign key (jid) references merge_job_des_html(jid);

--relationship between merge_job_post_date and merge_job_des_html
alter table merge_job_post_date add constraint fk_merge_job_post_date foreign key (jid) references merge_job_des_html(jid);





