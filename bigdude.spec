name: bigdude
summary: provides app to practice tlb optimization
license: GPLv2

version: 0.2
release: 1%{?dist}

group: Applications/Engineering
source: %{name}-%{version}.tar.gz
buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

buildrequires: gcc

# strace is needed to follow the exercise in the 
# README.asciidoc that accompanies bigdude
requires: strace
requires: bc

%description
Practice optimizing TLB cache, hugepages, mmap(2),
and hugetlbfs

%prep
%setup -q

%build
gcc src/hugedemo.c -o bigdude
chmod 755 bigdude

%install
%{__rm} -fr %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -pm755 bigdude %{buildroot}%{_bindir}

%clean
%{__rm} -fr %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/bigdude
%doc COPYING
%doc src/hugedemo.c
%doc README.asciidoc

%changelog
* Wed Oct 13 2010 Paul Morgan <jumanjiman@gmail.com> 0.1-1
- repackaged for open distribution
- added README.asciidoc with simple procedure

