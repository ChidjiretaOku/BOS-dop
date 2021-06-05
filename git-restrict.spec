Name:          git-restrict 
Version:       1.0
Release:       1%{?dist}
Summary:       security tool
Group:         Testing
License:       GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007
URL:           https://github.com/parazyd/git-restrict
Source0:       %{name}-%{version}.tar.gz
BuildRequires: gcc
Requires:      git, ssh

%description
A minimal utility that allows repository permission management based on ssh keys when used with the command directive in ssh's authorized_keys file.

%prep
%setup -q

%build 
gcc -g git-restrict.c -o git-restrict

%install
mkdir -p %{buildroot}%{_bindir}
cp git-restrict %{buildroot}%{_bindir}

%files
%{_bindir}/git-restrict

%changelog
* Sat Jun 05 2021 <Magoyan>
- Added %{_bindir}/git-restrict
