# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 07:50:25 2016

@author: efeariaroo
"""

import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from jenkinsapi.jenkins import Jenkins
from models import JenkinsJobsStatus


jenkins = Jenkins('https://jenkins.qa.ubuntu.com/api/python/')

dbpath = 'sqlite:///jenkins_jobs_statuses.db'
Session = sessionmaker()

def initialize_table():
    engine = create_engine(dbpath)
    JenkinsJobsStatus.Base.metadata.create_all(engine)
    Session.configure(bind=engine)

    if engine.dialect.has_table(engine, JenkinsJobsStatus.JobStatus.__tablename__):
        print(JenkinsJobsStatus.JobStatus.__tablename__ + " table EXISTS.\n")
    else:
        print(JenkinsJobsStatus.JobStatus.__tablename__ + " table does NOT EXIST.\n")

def get_jobs_names ():
    jobs_names_list = jenkins.keys()

    if len(jobs_names_list) > 10:
        jobs_names_list = jobs_names_list[0:10]

    return jobs_names_list

def start():
    initialize_table()

    try:
        jobs_names_list = get_jobs_names()
        session = Session()

        for job_name in jobs_names_list:
            jenkins_job = jenkins.get_job(job_name)
            job_last_build = jenkins_job.get_last_build()

            print("Job name: " + job_name + ", Build number: " + str(job_last_build.buildno) \
                + ", status: " + job_last_build.get_status())

            a_new_job_status = JenkinsJobsStatus.JobStatus(job_name, job_last_build.get_status())
            session.add(a_new_job_status)

        session.commit()
    except:
        print("Unexpected error:" + sys.exc_info()[0] + "\n")


if __name__ == '__main__':
    start()
