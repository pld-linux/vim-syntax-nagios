
%define		_vimdatadir	%{_datadir}/vim/vimfiles

Summary:	Vim plugin: Nagios configuration files syntax
Name:		vim-syntax-nagios
Version:	20050105
Release:	0.6
License:	as-is
Group:		Applications/Editors/Vim
Source0:	http://dev.gentoo.org/~ramereth/vim/syntax/nagios.vim
# Source0-md5:	cb76e1cc0825155c16b4891bddb3fb19
Requires:	%{_vimdatadir}
Requires:	vim >= 4:6.3.058-2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin provides syntax highlighting for Nagios configuration
files. Detection is by filename (/etc/nagios/).

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/{syntax,plugin,ftplugin,ftdetect}
install %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/syntax

cat > $RPM_BUILD_ROOT%{_vimdatadir}/ftdetect/%{name}.vim <<-EOF
au BufNewFile,BufRead /*etc/nagios/*.cfg set filetype=nagios
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/syntax/*
%{_vimdatadir}/ftdetect/*
