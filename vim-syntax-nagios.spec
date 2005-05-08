
%define		_vimdatadir	%{_datadir}/vim/vimfiles

Summary:	Vim plugin: Nagios configuration files syntax
Summary(pl):	Wtyczka Vima: pod¶wietlanie sk³adni dla plików konfiguracyjnych Nagiosa
Name:		vim-syntax-nagios
Version:	20050105
Release:	7
License:	as-is
Group:		Applications/Editors/Vim
Source0:	http://dev.gentoo.org/~ramereth/vim/syntax/nagios.vim
# Source0-md5:	cb76e1cc0825155c16b4891bddb3fb19
Patch0:		%{name}-fixes.patch
URL:		http://bugs.gentoo.org/show_bug.cgi?id=76712
# for _vimdatadir existence
Requires:	vim >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin provides syntax highlighting for Nagios configuration
files. Detection is by filename (/etc/nagios/).

%description -l pl
Ta wtyczka dostarcza pod¶wietlanie sk³adni dla plików konfiguracyjnych
Nagiosa. Pliki s± rozpoznawane po nazwie (/etc/nagios/).

%prep
%setup -q -c -T
install %{SOURCE0} .
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,plugin,ftplugin,ftdetect}
install nagios.vim $RPM_BUILD_ROOT%{_vimdatadir}/syntax

cat > $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{name}.vim <<-EOF
au BufNewFile,BufRead /*etc/nagios/*.cfg,*sample-config/template-object/*.cfg{,.in},/var/lib/nagios/objects.cache set filetype=nagios
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
