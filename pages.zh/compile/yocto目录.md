在执行bitbake编译前：

├── bitbake--主要包含bitbake脚本，作为Metadata解析器，读取Yocto Metadata并运行其定义的task。
├── build--主要包含用户配置文件，并将编译输出到此目录。
├── contrib--
├── documentation--帮助文档，可以生成pdf或者html版本用户手册。
├── LICENSE--License声明。
├── LICENSE.GPL-2.0-only
├── LICENSE.MIT
├── MEMORIAM
├── meta--对应OpenEmbedded-Core的Metadata，包含Recipes、Classes，以及qemux86/qemuarm的机器配置。
├── meta-poky--在meta目录基础上，增加Poky参考发布版本的必须Metadata。
├── meta-selftest--OpenEmbedded验证编译系统的selftest的Recipes和Append文件。
├── meta-skeleton--BSP和Kernel开发的Recipes模板。
├── meta-yocto-bsp--Yocto项目的参考BSP Metadata。
├── oe-init-build-env--设置OpenEmbedded编译环境的脚本。
├── README.hardware -> meta-yocto-bsp/README.hardware
├── README.OE-Core
├── README.poky -> meta-poky/README.poky
├── README.qemu
└── scripts--Yocto项目附加功能所需要的脚本。

在执行bitbake编译后，在build目录下会生成一系列目录：
build/
├── bitbake-cookerdaemon.log
├── cache
│   ├── bb_codeparser.dat
│   ├── bb_persist_data.sqlite3
│   ├── bb_unihashes.dat
│   ├── hashserv.db
│   ├── hashserv.db-shm
│   ├── hashserv.db-wal
│   ├── local_file_checksum_cache.dat
│   └── sanity_info
├── conf
│   ├── bblayers.conf--配置了bitbake查找layers所需要遍历的目录，定义在BBLAYERS中。
│   ├── local.conf--用户编译环境配置文件。
│   └── templateconf.cfg
├── downloads--存放下载的源码。
├── sstate-cache--shares state cache。
└── tmp--编译系统存放所有的编译输出。
    ├── abi_version
    ├── buildstats--build statistics。
    ├── cache--缓存解析Metadata的结果，包括Recipes和配置文件。
    ├── deploy--保存OpenEmbedded编译过程的结果。
        ├── images--生成的镜像文件。
        ├── licenses
        └── rpm--rpm安装包。
    ├── hosttools--指向编译主机的程序。
    ├── log--编译日志文件。
    ├── pkgdata
    ├── saved_tmpdir
    ├── sstate-control
    ├── stamps--bitbake task运行时间戳。
    ├── sysroots-components--do_prepare_recipe_sysroot任务拷贝相应Recipe的sysroot内容。
    ├── sysroots-uninative--非本地编译的sysroot内容。
    ├── work--包含bitbake编译架构相关包子目录。
        ├──qemux86_64-poky-linux/core-image-minimal/1.0-r0/rootfs--各仓库编译安装到rootfs中，然后打包生成镜像。
    └── work-shared