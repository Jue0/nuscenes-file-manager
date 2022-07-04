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
from ast import arg
import logging
import tarfile

import os
import glob
import csv



if __name__=='__main__':
    ju=0

    logger = logging.getLogger()

    parser = argparse.ArgumentParser(description='인자값 받기')
    parser.add_argument('--src', required=True, help='압축파일들 있는 경로')    
    parser.add_argument('--dst', required=True, help='압축해제할 경로')    

    args = parser.parse_args()
    logger.info(args.src)
    logger.info(args.dst)
    
    filelist = glob.glob(args.src+"/*.tar") + glob.glob(args.src+"/*.tgz")
    # print(filelist)
    # logger.info(filelist)

    ## output 파일 열고, 파일 이름 로깅
    with open(args.src+'/output.txt', 'a') as output:
        for f in filelist:
            if f.split('.')[1]=='tgz':
                # print(f.split('.')[1])
                logger.info(f.split('.')[1])
                file = tarfile.open(f, 'r:gz')
            else:
                # print(f.split('.')[1])
                logger.info(f.split('.')[1])
                file = tarfile.open(f, 'r')

            names = file.getnames()
            num_names = len(names)
            # print(*names, sep='\n')
            # print(names)
            for line in names:
                output.write(line+'\n')
            # output.writelines(names)
            l = '_____' + os.path.basename(f) + ' total {} files'.format(num_names)
            output.write(l+ '\n\n')
            
            file.close()
            
    ## 압축파일 해제
