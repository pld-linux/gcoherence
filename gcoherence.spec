Summary:	A simple free media server
Name:		gcoherence
Version:	0.1.0
Release:	2
License:	GPL v3
Group:		X11/Applications
Source0:	http://29a.ch/gcoherence/%{name}-%{version}.tar.gz
# Source0-md5:	fe71cb048cb19e0947e7f1c78b37e48d
URL:		http://29a.ch/gcoherence/
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	python-pygtk-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	python-coherence
Requires:	python-pygtk-gtk
Requires:	python-pyxdg
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple free media server.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

install -d $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps
mv $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/{,apps/}gcoherence.png

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%find_lang gcoherence --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post
%update_icon_cache hicolor

%postun
%update_desktop_database_postun
%update_icon_cache hicolor

%files -f gcoherence.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gcoherence
%{py_sitescriptdir}/x29a
%{py_sitescriptdir}/%{name}-%{version}-py*.egg-info
%{_desktopdir}/gcoherence.desktop
%{_iconsdir}/hicolor/*/apps/gcoherence.png
%{_pixmapsdir}/gcoherence.png
