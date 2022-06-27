#-*- coding:utf-8 -*-
'''
Jue0, 22.06.27. ~

A simple file manager for managing all compressed files 
    in the nuscens dataset and managing individual files.

input: 1) Source path where the compressed files to be released exist
       2) Destination path for decompressed files
output: Files extracted from compressed files, 
        csv files containing file names by compressed file

#goal : argparse, logger, 압축파일해제하는 라이브러리 사용
#1 argparse로 입력받은 경로 접근
#2 파일목록 받아서 하나씩 loop
#3 loop: 압축 해제, 파일 개수 세고, 그걸 csv에 압축파일명과 함께 기록
    0열= loop 번호(1부터) 1열=압축파일명 2열=sweeps/samples 3열=센서 4열=개별파일명
#4 압축파일 별 파일트리마다 파일 개수 기록, 출력
'''

## 라이브러리
import argparse
import logging
import tarfile

import os
import csv



def main():
    ju=0
    

main()