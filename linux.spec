#
# note to self: Linus releases need to be named 4.x.0 not 4.x or various
# things break
#

Name:           linux
Version:        4.16.9
Release:        571
License:        GPL-2.0
Summary:        The Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source0:        https://www.kernel.org/pub/linux/kernel/v4.x/linux-4.16.9.tar.xz
Source1:        config
Source2:        cmdline

%define ktarget  native
%define kversion %{version}-%{release}.%{ktarget}

BuildRequires:  bash >= 2.03
BuildRequires:  bc
BuildRequires:  binutils-dev
BuildRequires:  elfutils-dev
BuildRequires:  make >= 3.78
BuildRequires:  openssl-dev
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  kmod
BuildRequires:  linux-firmware
BuildRequires:  kernel-install

Requires: systemd-console

# don't strip .ko files!
%global __os_install_post %{nil}
%define debug_package %{nil}
%define __strip /bin/true

#    000X: cve, bugfixes patches


#    00XY: Mainline patches, upstream backports

Patch0040: 0001-idle-from-rafael.patch
Patch0041: 0002-idle-from-rafael.patch

Patch0051: 0001-time-tick-sched-Reorganize-idle-tick-management-code.patch
Patch0052: 0002-sched-idle-Do-not-stop-the-tick-upfront-in-the-idle-.patch
Patch0053: 0003-sched-idle-Do-not-stop-the-tick-before-cpuidle_idle_.patch
Patch0054: 0004-jiffies-Introduce-USER_TICK_USEC-and-redefine-TICK_U.patch
Patch0055: 0005-cpuidle-Return-nohz-hint-from-cpuidle_select.patch
Patch0056: 0006-time-tick-sched-Split-tick_nohz_stop_sched_tick.patch
Patch0057: 0007-time-hrtimer-Introduce-hrtimer_next_event_without.patch
Patch0058: 0008-sched-idle-Select-idle-state-before-stopping-the-tic.patch
Patch0059: 0009-cpuidle-menu-Refine-idle-state-selection-for-running.patch
Patch0060: 0010-cpuidle-menu-Avoid-selecting-shallow-states-with-sto.patch
Patch0061: 0011-nohz-Gather-tick_sched-booleans-under-a-common-flag-.patch
Patch0062: 0012-nohz-Avoid-duplication-of-code-related-to-got_idle_t.patch
Patch0063: 0013-time-hrtimer-Use-timerqueue_iterate_next-to-get-to-t.patch
Patch0064: 0099-fixup-idle.patch


# Serie    01XX: Clear Linux patches
Patch0101: 0101-i8042-decrease-debug-message-level-to-info.patch
Patch0102: 0102-init-do_mounts-recreate-dev-root.patch
Patch0103: 0103-Increase-the-ext4-default-commit-age.patch
Patch0104: 0104-silence-rapl.patch
Patch0105: 0105-pci-pme-wakeups.patch
Patch0106: 0106-ksm-wakeups.patch
Patch0107: 0107-intel_idle-tweak-cpuidle-cstates.patch
Patch0108: 0108-xattr-allow-setting-user.-attributes-on-symlinks-by-.patch
Patch0110: 0110-fs-ext4-fsync-optimize-double-fsync-a-bunch.patch
Patch0111: 0111-overload-on-wakeup.patch
Patch0112: 0112-bootstats-add-printk-s-to-measure-boot-time-in-more-.patch
Patch0113: 0113-fix-initcall-timestamps.patch
Patch0114: 0114-smpboot-reuse-timer-calibration.patch
Patch0115: 0115-raid6-add-Kconfig-option-to-skip-raid6-benchmarking.patch
Patch0116: 0116-Initialize-ata-before-graphics.patch
Patch0117: 0117-reduce-e1000e-boot-time-by-tightening-sleep-ranges.patch
Patch0118: 0118-give-rdrand-some-credit.patch
Patch0120: 0120-ipv4-tcp-allow-the-memory-tuning-for-tcp-to-go-a-lit.patch
Patch0121: 0121-igb-no-runtime-pm-to-fix-reboot-oops.patch
Patch0122: 0122-tweak-perfbias.patch
Patch0123: 0123-e1000e-increase-pause-and-refresh-time.patch
Patch0124: 0124-kernel-time-reduce-ntp-wakeups.patch
Patch0125: 0125-init-wait-for-partition-and-retry-scan.patch
Patch0126: 0126-print-fsync-count-for-bootchart.patch
Patch0127: 0127-Add-boot-option-to-allow-unsigned-modules.patch

# Clear Linux KVM Memory Optimization
Patch0151: 0151-mm-Export-do_madvise.patch
Patch0152: 0152-x86-kvm-Notify-host-to-release-pages.patch
Patch0153: 0153-x86-Return-memory-from-guest-to-host-kernel.patch
Patch0154: 0154-sysctl-vm-Fine-grained-cache-shrinking.patch

#
# Small tweaks
#

Patch0500: zero-regs.patch
Patch0501: itmt.patch
Patch0503: spinfaster.patch
Patch0504: try_load_dmc.patch
Patch0505: clip-idle-prediction.patch


#    200X: Open Programmable Acceleration Engine (OPAE)
Patch2001: 2001-opae-add-intel-fpga-drivers.patch
Patch2002: 2002-opae-add-Kconfig-and-Makefile.patch

#    300X: Sysdig
Patch3001: 3001-Add-sysdig-0.20-driver.patch
Patch3002: 3002Add-sysdig-to-kernel-build-system.patch

%description
The Linux kernel.

%package extra
License:        GPL-2.0
Summary:        The Linux kernel extra files
Group:          kernel

%description extra
Linux kernel extra files

%package clr-init
License:        GPL-2.0
Summary:        Symlink to clr-init file
Group:          kernel

%description clr-init
Generates a symlink to the clr-init file to boot with encrypted root partion.

%package dev
License:        GPL-2.0
Summary:        The Linux kernel
Group:          kernel
Requires:       %{name} = %{version}-%{release}, %{name}-extra = %{version}-%{release}

%description dev
Linux kernel build files and install script

%prep
%setup -q -n linux-4.16.9

#     000X  cve, bugfixes patches

#     00XY  Mainline patches, upstream backports

%patch0040 -p1
%patch0041 -p1


%patch0051 -p1
%patch0052 -p1
%patch0053 -p1
%patch0054 -p1
%patch0055 -p1
%patch0056 -p1
%patch0057 -p1
%patch0058 -p1
%patch0059 -p1
%patch0060 -p1
%patch0061 -p1
%patch0062 -p1
%patch0063 -p1
%patch0064 -p1



#     01XX  Clear Linux patches
%patch0101 -p1
%patch0102 -p1
%patch0103 -p1
%patch0104 -p1
%patch0105 -p1
%patch0106 -p1
%patch0107 -p1
%patch0108 -p1
%patch0110 -p1
%patch0111 -p1
%patch0112 -p1
%patch0113 -p1
%patch0114 -p1
#%patch0115 -p1
%patch0116 -p1
%patch0117 -p1
%patch0118 -p1
%patch0120 -p1
%patch0121 -p1
%patch0122 -p1
%patch0123 -p1
%patch0124 -p1
%patch0125 -p1
%patch0126 -p1
%patch0127 -p1

# Clear Linux KVM Memory Optimization
%patch0151 -p1
%patch0152 -p1
%patch0153 -p1
%patch0154 -p1


%patch0500 -p1
%patch0501 -p1
%patch0503 -p1
%patch0504 -p1
%patch0505 -p1

#    200X: Open Programmable Acceleration Engine (OPAE)
#%patch2001 -p1
#%patch2002 -p1

#	300X: sysdig
%patch3001 -p1
%patch3002 -p1


cp %{SOURCE1} .

cp -a /usr/lib/firmware/i915 firmware/
cp -a /usr/lib/firmware/intel-ucode firmware/

%build
BuildKernel() {

    Target=$1
    Arch=x86_64
    ExtraVer="-%{release}.${Target}"

    perl -p -i -e "s/^EXTRAVERSION.*/EXTRAVERSION = ${ExtraVer}/" Makefile

    make O=${Target} -s mrproper
    cp config ${Target}/.config

    make O=${Target} -s ARCH=${Arch} olddefconfig
    make O=${Target} -s ARCH=${Arch} CONFIG_DEBUG_SECTION_MISMATCH=y %{?_smp_mflags} %{?sparse_mflags}
}

BuildKernel %{ktarget}

%install

InstallKernel() {

    Target=$1
    Kversion=$2
    Arch=x86_64
    KernelDir=%{buildroot}/usr/lib/kernel

    mkdir   -p ${KernelDir}
    install -m 644 ${Target}/.config    ${KernelDir}/config-${Kversion}
    install -m 644 ${Target}/System.map ${KernelDir}/System.map-${Kversion}
    install -m 644 ${Target}/vmlinux    ${KernelDir}/vmlinux-${Kversion}
    install -m 644 %{SOURCE2}           ${KernelDir}/cmdline-${Kversion}
    cp  ${Target}/arch/x86/boot/bzImage ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}
    chmod 755 ${KernelDir}/org.clearlinux.${Target}.%{version}-%{release}

    mkdir -p %{buildroot}/usr/lib/modules
    make O=${Target} -s ARCH=${Arch} INSTALL_MOD_PATH=%{buildroot}/usr modules_install

    rm -f %{buildroot}/usr/lib/modules/${Kversion}/build
    rm -f %{buildroot}/usr/lib/modules/${Kversion}/source
    DevDir=%{buildroot}/usr/lib/modules/${Kversion}/build
    mkdir -p ${DevDir}
    find . -type f -a '(' -name 'Makefile*' -o -name 'Kbuild*' -o -name 'Kconfig*' ')' -exec cp -t ${DevDir} --parents -pr {} +
    find . -type f -a '(' -name '*.sh' -o -name '*.pl' ')' -exec cp -t ${DevDir} --parents -pr {} +
    cp -t ${DevDir} -pr ${Target}/{Module.symvers,tools}
    ln -s ../../../kernel/config-${Kversion} ${DevDir}/.config
    ln -s ../../../kernel/System.map-${Kversion} ${DevDir}/System.map
    cp -t ${DevDir} --parents -pr arch/x86/include
    cp -t ${DevDir}/arch/x86/include -pr ${Target}/arch/x86/include/*
    cp -t ${DevDir}/include -pr include/*
    cp -t ${DevDir}/include -pr ${Target}/include/*
    cp -t ${DevDir} --parents -pr scripts/*
    cp -t ${DevDir}/scripts -pr ${Target}/scripts/*
    find  ${DevDir}/scripts -type f -name '*.[cho]' -exec rm -v {} +
    find  ${DevDir} -type f -name '*.cmd' -exec rm -v {} +
    # Cleanup any dangling links
    find ${DevDir} -type l -follow -exec rm -v {} +

    ln -s org.clearlinux.${Target}.%{version}-%{release} %{buildroot}/usr/lib/kernel/default-${Target}
    ln -s clr-init.img.gz %{buildroot}/usr/lib/kernel/initrd-org.clearlinux.${Target}.%{version}-%{release}
}

InstallKernel %{ktarget}  %{kversion}

rm -rf %{buildroot}/usr/lib/firmware

%files
%dir /usr/lib/kernel
%dir /usr/lib/modules/%{kversion}
/usr/lib/kernel/config-%{kversion}
/usr/lib/kernel/cmdline-%{kversion}
/usr/lib/kernel/org.clearlinux.%{ktarget}.%{version}-%{release}
/usr/lib/kernel/default-%{ktarget}
/usr/lib/modules/%{kversion}/kernel
/usr/lib/modules/%{kversion}/modules.*

%files extra
%dir /usr/lib/kernel
/usr/lib/kernel/System.map-%{kversion}
/usr/lib/kernel/vmlinux-%{kversion}

%files clr-init
%dir /usr/lib/kernel
/usr/lib/kernel/initrd-org.clearlinux.%{ktarget}.%{version}-%{release}

%files dev
%defattr(-,root,root)
/usr/lib/modules/%{kversion}/build
