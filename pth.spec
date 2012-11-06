##
##  GNU Pth - The GNU Portable Threads
##  Copyright (c) 2000-2006 Ralf S. Engelschall <rse@engelschall.com>
##
##  This file is part of GNU Pth, a non-preemptive thread scheduling
##  library which can be found at http://www.gnu.org/software/pth/.
##
##  This library is free software; you can redistribute it and/or
##  modify it under the terms of the GNU Lesser General Public
##  License as published by the Free Software Foundation; either
##  version 2.1 of the License, or (at your option) any later version.
##
##  This library is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
##  Lesser General Public License for more details.
##
##  You should have received a copy of the GNU Lesser General Public
##  License along with this library; if not, write to the Free Software
##  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
##  USA, or contact Ralf S. Engelschall <rse@engelschall.com>.
##
##  pth.spec: RPM specification
##

#   This is a specification file for the RedHat Package Manager (RPM).
#   It is part of the Pth source tree and this way directly included in
#   Pth distribution tarballs. This way one can use a simple `rpm -tb
#   pth-1.X.Y.tar.gz' command to build binary RPM packages from a Pth
#   distribution tarball.

%define ver 2.0.7
%define rel 2

Name:       pth
Version:    %{ver}
Release:    %{rel}
Group:      System Environment/Libraries
License:    LGPL
URL:        http://www.gnu.org/software/pth/
Summary:    GNU Pth - The GNU Portable Threads

Source:     ftp://ftp.gnu.org/gnu/pth/pth-%{ver}.tar.gz
Patch1:     pth-2.0.7-libdir.patch
Prefix:     %{_prefix}
BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Pth is a very portable POSIX/ANSI-C based library for Unix platforms which
provides non-preemptive priority-based scheduling for multiple threads of
execution (aka ``multithreading'') inside event-driven applications. All
threads run in the same address space of the server application, but each
thread has it's own individual program-counter, run-time stack, signal
mask and errno variable.

The thread scheduling itself is done in a cooperative way, i.e., the
threads are managed by a priority- and event-based non-preemptive
scheduler. The intention is that this way one can achieve better
portability and run-time performance than with preemptive scheduling. The
event facility allows threads to wait until various types of events occur,
including pending I/O on filedescriptors, asynchronous signals, elapsed
timers, pending I/O on message ports, thread and process termination, and
even customized callback functions.

Additionally Pth provides an optional emulation API for POSIX.1c threads
("Pthreads") which can be used for backward compatibility to existing
multithreaded applications.

%package devel
Summary: GNU Pth development package
Group: Development/Libraries
Requires: pth = %{ver}

%description devel
Headers, static libraries, and documentation for GNU Portable Threads.

%prep

%setup

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-optimize --enable-pthread
make
make test

%install
make install prefix=$RPM_BUILD_ROOT%{_prefix} libdir=$RPM_BUILD_ROOT%{_libdir} mandir=$RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc ANNOUNCE AUTHORS COPYING ChangeLog HACKING HISTORY INSTALL NEWS PORTING README SUPPORT TESTS THANKS USERS
%{_libdir}/libpth.so
%{_libdir}/libpth.so.*
%{_libdir}/libpthread.so
%{_libdir}/libpthread.so.*

%files devel
%defattr(-,root,root)
%{_bindir}/pth-config
%{_bindir}/pthread-config
%{_includedir}/pth.h
%{_includedir}/pthread.h
%{_libdir}/libpth.a
%{_libdir}/libpth.la
%{_libdir}/libpthread.a
%{_libdir}/libpthread.la
%{_mandir}/man1/pth-config.1*
%{_mandir}/man1/pthread-config.1*
%{_mandir}/man3/pth.3*
%{_mandir}/man3/pthread.3*
%{_datadir}/aclocal/pth.m4

