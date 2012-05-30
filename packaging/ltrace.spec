Name:       ltrace
Summary:    Tracks runtime library calls in dynamically linked programs
Version:    0.5.3
Release:    1
Group:      utils
License:    GPLv1
Source0:    ltrace-0.5.3.tar.gz
Source1001: packaging/ltrace.manifest 
BuildRequires:  binutils-devel
BuildRequires:  elfutils-libelf-devel


%description
Tracks runtime library calls in dynamically linked programs
 ltrace is a debugging program which runs a specified command until it
 exits.  While the command is executing, ltrace intercepts and records
 the dynamic library calls which are called by
 the executed process and the signals received by that process.
 It can also intercept and print the system calls executed by the program.
 .
 The program to be traced need not be recompiled for this, so you can
 use it on binaries for which you don't have the source handy.
 .
 You should install ltrace if you need a sysadmin tool for tracking the
 execution of processes..

%prep
%setup -q

%build
cp %{SOURCE1001} .

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
rm -rf %{buildroot}%{_prefix}/share/doc/ltrace

%files
%manifest ltrace.manifest
%defattr(-,root,root,-)
%doc README COPYING
%{_sysconfdir}/ltrace.conf
%{_bindir}/ltrace
%{_mandir}/man1/ltrace.1.gz
