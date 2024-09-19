/*
 * @Author: 0xSchnappi 952768182@qq.com
 * @Date: 2024-09-19 17:20:43
 * @LastEditors: 0xSchnappi 952768182@qq.com
 * @LastEditTime: 2024-09-19 17:32:39
 * @FilePath: /msic/angr-script/02-example/example.c
 * @Description: 基本使用
 * https://bbs.kanxue.com/thread-268251-1.htm
 *
 * Copyright (c) 2024 by github.com/0xSchnappi, All Rights Reserved.
 */
#include <stdio.h>
#include <stdlib.h>

void main(int argc, char *argv[]) {
  int a = atoi(argv[1]);
  int b = atoi(argv[2]);
  if (10 > a && a > 5 && 10 > b && b > 1 && 2 * b - a == 10) {
    printf("[+] Math is hard... but not 4 u!\n");
  }
}