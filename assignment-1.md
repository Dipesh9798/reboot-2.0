## Solution 1-->





--------------------------------------------------------------------------------

## Solution 2--->

>>create a directory without name from command line-->
>>mkdir " "

>>create a directory with name "-okgoogle"-->
>>mkdir ./-okgoogle

--------------------------------------------------------------------------------

## Solution 3--->

>>create a directory structure

![prob3](https://user-images.githubusercontent.com/44002665/87472025-e6c18100-c63c-11ea-8221-3eb6fd97fec2.png)

>> mkdir -p A/{B/{G/K,H/J},C/{I/J,J/L},D/{E/M,F/L}}/Reboot.txt

![Screenshot from 2020-07-15 01-28-25](https://user-images.githubusercontent.com/44002665/87471217-9eee2a00-c63b-11ea-8627-0e851885dd42.png)


-------------------------------------------------------------------------------

## Solution 4--->

## (a)create two users name jack and jill from command line
```
[dipesh@localhost ~]$ sudo useradd Jack
[sudo] password for dipesh: 
[dipesh@localhost ~]$ sudo passwd Jack
Changing password for user Jack.
New password: 
BAD PASSWORD: The password is a palindrome
Retype new password: 
passwd: all authentication tokens updated successfully.

[dipesh@localhost ~]$ sudo useradd Jill
[dipesh@localhost ~]$ sudo passwd Jill
Changing password for user Jill.
New password: 
BAD PASSWORD: The password is a palindrome
Retype new password: 
passwd: all authentication tokens updated successfully.

```
### (b)login with jack user and create a file name  jack.txt using vim editor and write "hello jack"
```
[Jack@localhost ~]$ vim Jack.txt
[Jack@localhost ~]$ cat Jack.txt 
Hello Jack
```
### (c)from jack user also create two directories name jack1 & jack2 
```
[Jack@localhost ~]$ pwd
/home/Jack
[Jack@localhost ~]$ mkdir jack1 jack2
[Jack@localhost ~]$ ls
jack1  jack2  Jack.txt

```
## (d)now login from Jill user and create a file. Jill.txt using vim editor and write "hey jiil"
```
[Jill@localhost ~]$ vim Jill.txt
[Jill@localhost ~]$ cat Jill.txt
hey jill

```
## (e)from Jill also create two directoires named jill1 & jill2 
```
[Jill@localhost ~]$ mkdir jill1 jill2
[Jill@localhost ~]$ ls
jill1  jill2  Jill.txt

```
## (f)swap these files and directories in between users  and to swap don't use root account.
```
[Jill@localhost ~]$ chmod 777 -R /home/Jill/
[Jill@localhost ~]$ ls -l
total 12
drwxrwxrwx. 2 Jill Jill 4096 Jul 15 02:30 jill1
drwxrwxrwx. 2 Jill Jill 4096 Jul 15 02:30 jill2
-rwxrwxrwx. 1 Jill Jill    9 Jul 15 02:28 Jill.txt

[Jill@localhost ~]$ su - Jack
Password: 
[Jack@localhost ~]$ chmod 777 -R /home/Jack/
[Jack@localhost ~]$ ls -l
total 12
drwxrwxrwx. 2 Jack Jack 4096 Jul 15 02:25 jack1
drwxrwxrwx. 2 Jack Jack 4096 Jul 15 02:25 jack2
-rwxrwxrwx. 1 Jack Jack   11 Jul 15 02:23 Jack.txt

[Jack@localhost ~]$ mv /home/Jill/jill1 /home/Jack/
[Jack@localhost ~]$ mv /home/Jill/jill2 /home/Jack/
[Jack@localhost ~]$ mv /home/Jill/Jill.txt /home/Jack/
[Jack@localhost ~]$ ls
jack1  jack2  Jack.txt  jill1  jill2  Jill.txt

[Jack@localhost ~]$ su - Jill
Password: 
[Jill@localhost ~]$ mv /home/Jack/jack1 /home/Jill/
[Jill@localhost ~]$ mv /home/Jack/jack2 /home/Jill/
[Jill@localhost ~]$ mv /home/Jack/Jack.txt /home/Jill/
[Jill@localhost ~]$ ls
jack1  jack2  Jack.txt  jill1  jill2  Jill.txt

```

## Solution #5 :  play with files and directories 

## (a)create  3 files named   abc.txt  ok  fine  g.txt  /tmp directory 
```
[dipesh@localhost ~]$ touch /tmp/{abc.txt,ok,fine,g.txt}
[dipesh@localhost ~]$ ls /tmp/
abc.txt
fine
g.txt
ok
systemd-private-b80e1968a92e4627a5b016cc1f25918f-chronyd.service-izm0oj
systemd-private-b80e1968a92e4627a5b016cc1f25918f-colord.service-FrSKPf
systemd-private-b80e1968a92e4627a5b016cc1f25918f-dbus-broker.service-wQr58i
systemd-private-b80e1968a92e4627a5b016cc1f25918f-earlyoom.service-irJqTf
systemd-private-b80e1968a92e4627a5b016cc1f25918f-fwupd.service-9GtQQi
systemd-private-b80e1968a92e4627a5b016cc1f25918f-geoclue.service-FjaSxg
systemd-private-b80e1968a92e4627a5b016cc1f25918f-ModemManager.service-KJxkig
systemd-private-b80e1968a92e4627a5b016cc1f25918f-rtkit-daemon.service-1PcFSi
systemd-private-b80e1968a92e4627a5b016cc1f25918f-switcheroo-control.service-YtRbqg
systemd-private-b80e1968a92e4627a5b016cc1f25918f-systemd-logind.service-5Lapwh
systemd-private-b80e1968a92e4627a5b016cc1f25918f-upower.service-aLgm1e
Temp-9a8c7498-3e87-4338-86b1-c6f0d4783a55
Temp-9da140d6-c0c0-4f9a-91c8-6a179ccb505c
tracker-extract-files.1000


```
## (b)create  4  directories   aa aaa aaaa  under  /tmp directory 
```
[dipesh@localhost ~]$ mkdir /tmp/{aa,aaa,aaaa}
[dipesh@localhost ~]$ ls /tmp/
aa
aaa
aaaa
abc.txt
fine
g.txt
ok
systemd-private-b80e1968a92e4627a5b016cc1f25918f-chronyd.service-izm0oj
systemd-private-b80e1968a92e4627a5b016cc1f25918f-colord.service-FrSKPf
systemd-private-b80e1968a92e4627a5b016cc1f25918f-dbus-broker.service-wQr58i
systemd-private-b80e1968a92e4627a5b016cc1f25918f-earlyoom.service-irJqTf
systemd-private-b80e1968a92e4627a5b016cc1f25918f-fwupd.service-9GtQQi
systemd-private-b80e1968a92e4627a5b016cc1f25918f-geoclue.service-FjaSxg
systemd-private-b80e1968a92e4627a5b016cc1f25918f-ModemManager.service-KJxkig
systemd-private-b80e1968a92e4627a5b016cc1f25918f-rtkit-daemon.service-1PcFSi
systemd-private-b80e1968a92e4627a5b016cc1f25918f-switcheroo-control.service-YtRbqg
systemd-private-b80e1968a92e4627a5b016cc1f25918f-systemd-logind.service-5Lapwh
systemd-private-b80e1968a92e4627a5b016cc1f25918f-upower.service-aLgm1e
Temp-9a8c7498-3e87-4338-86b1-c6f0d4783a55
Temp-9da140d6-c0c0-4f9a-91c8-6a179ccb505c
tracker-extract-files.1000

```
## (c)  give ls command to  list the content of  /tmp directory and  make sure it will only list the content (file|directory)  having 2 char in their name.
```

```


## Solution #7 :    create a shell script

## create a shell script named /root/delvex.sh
```
[root@localhost ~]# vim /root/delvex.sh


```

##   make sure it will run /bin/sh shell 
```
[root@localhost ~]# cat delvex.sh 
#!/bin/sh

```
##  a user will be running this script my using a command name opensource
```
[root@localhost ~]# vim /usr/bin/opensource
#!/bin/bash

/root/delvex.sh $1
~                                                                                                            
~                                                                                                            
~                                                                                                            
~                                                                                                            
~                                                                                                            
~                                                                                                                                                                                                              
~                                                                                                            
-- INSERT --                                                                               3,18          All

[root@localhost ~]# chmod +x /root/delvex.sh
[root@localhost ~]# chmod +x /usr/bin/opensource


```
delvex.sh
```
#!/bin/sh

if [$# -gt 0]
then
	if [$1 == "time"]
	then
		echo "current time:`date +%T`"
	elif [$1 == "user"]
        then    
                echo "Users:`users`"
	elif [$1 == "100"]
        then    
		$c=$1
		while [ $c != 0 ]
		do
			echo "$c Hello Delvex"
			sleep 1
			c=$(($c-1))
		done
	elif [$1 == "windows"]
        then
                echo "Shutting Down System..."
		sleep 2
		shutdown now
	fi
else
	echo "Name of Kernel: `uname -s`"
	echo "Version of Kernel: `uname -r`"
	echo "Current date: `date +'%d/%m/%y'`"
	echo "Name of OS: `uname -o`"
	echo "Last Boot Time: `who -b | awk '{print $4}'`"
fi

```






