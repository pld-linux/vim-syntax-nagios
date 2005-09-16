
%define		_vimdatadir	%{_datadir}/vim/vimfiles

Summary:	Vim syntax: Nagios configuration files syntax
Summary(pl):	Opis sk³adni dla Vima: pod¶wietlanie sk³adni dla plików konfiguracyjnych Nagiosa
Name:		vim-syntax-nagios
Version:	20050105
Release:	9
License:	as-is
Group:		Applications/Editors/Vim
Source0:	nagios.vim
URL:		http://bugs.gentoo.org/show_bug.cgi?id=76712
# for _vimdatadir existence
Requires:	vim >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_syntax nagios

%description
This plugin provides syntax highlighting for Nagios configuration
files. Detection is by filename (/etc/nagios).

%description -l pl
Ta wtyczka dostarcza pod¶wietlanie sk³adni dla plików konfiguracyjnych
Nagiosa. Pliki s± rozpoznawane po nazwie (/etc/nagios).

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,ftdetect}
install %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/syntax

cat > $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{_syntax}.vim <<-EOF
au BufNewFile,BufRead /*etc/nagios/*.cfg,*sample-config/template-object/*.cfg{,.in},/var/lib/nagios/objects.cache set filetype=%{_syntax}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
