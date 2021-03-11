%define debug_package %{nil}

Name:           djview4
Version:        4.12
Release:        1
Summary:        DjVu viewer and browser plugin
License:        GPLv2+
Group:          Publishing
URL:            http://djvu.sourceforge.net/djview4.html
Source0:        https://sourceforge.net/projects/djvu/files/DjView/%{version}/djview-%{version}.tar.gz

BuildRequires:  qmake5
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libtiff-4)

%description
This package contains the djview4 viewer and browser plugin.

Highlights:

- Entirely based on the public djvulibre api.
- Entirely written in portable Qt4.
- Works with Qt/X11, Qt/Mac, and Qt/Windows.
- Continuous scrolling of pages.
- Side-by-side display of pages.
- Ability to specify a url to the djview command.
- All plugin and cgi options available from the command line.
- All silly annotations implemented.
- Display thumbnails as a grid.
- Display outlines.
- Page names supported (see djvused command set-page-title).
- Metadata dialog (see djvused command set-meta).
- Mmplemented as reusable Qt widgets.

%prep
%setup -q

%build
./autogen.sh
%configure --disable-nsdejavu
%make_build

%install
%make_install

ln -s %{_bindir}/djview %{buildroot}%{_bindir}/%{name}

%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{__cp} -a desktopfiles/prebuilt-hi32-%{name}.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/djvulibre-%{name}.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
%{__cp} -a desktopfiles/prebuilt-hi64-%{name}.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/djvulibre-%{name}.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
%{__cp} -a desktopfiles/djview.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/djvulibre-%{name}.svg

%{__cp} %{buildroot}%{_mandir}/man1/djview.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc COPYING COPYRIGHT NEWS README README_translations
%{_bindir}/djview
%{_bindir}/%{name}
%{_datadir}/djvu/%{name}/
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/djview.1*
%{_datadir}/applications/djvulibre-%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/djvulibre-%{name}.*
%{_datadir}/icons/hicolor/*/mimetypes/djvulibre-%{name}.*


%changelog
* Thu Oct 06 2011 Andrey Bondrov <abondrov@mandriva.org> 0:4.8-1
+ Revision: 703281
- Add patch0 to avoid swap function overloading
- New version: 4.8

* Wed Mar 09 2011 Lev Givon <lev@mandriva.org> 0:4.7-1
+ Revision: 643129
- Update to 4.7.

* Sat Feb 26 2011 Tomas Kindl <supp@mandriva.org> 0:4.6-2
+ Revision: 639824
- rebuilt

* Mon Nov 01 2010 Lev Givon <lev@mandriva.org> 0:4.6-1mdv2011.0
+ Revision: 591630
- Update to 4.6.
  Remove format string patch (no longer necessary).

* Wed Jul 28 2010 Lev Givon <lev@mandriva.org> 0:4.5-3mdv2011.0
+ Revision: 562702
- Include svg icon.

* Wed Mar 17 2010 Lev Givon <lev@mandriva.org> 0:4.5-2mdv2010.1
+ Revision: 524611
- Include high-resolution icon in package.

* Sat Dec 12 2009 Jérôme Brenier <incubusss@mandriva.org> 0:4.5-1mdv2010.1
+ Revision: 477780
- new version 4.5
- fix str fmt
- fix license tag

* Sat Oct 18 2008 David Walluck <walluck@mandriva.org> 0:4.4-1mdv2009.1
+ Revision: 295151
- 4.4

* Sun Sep 07 2008 Frederik Himpe <fhimpe@mandriva.org> 0:4.3-3mdv2009.0
+ Revision: 282360
- Rebuild for new djvulibre

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 0:4.3-2mdv2009.0
+ Revision: 266564
- rebuild early 2009.0 package (before pixel changes)

* Sun Apr 20 2008 David Walluck <walluck@mandriva.org> 0:4.3-1mdv2009.0
+ Revision: 196002
- 4.3

* Wed Jan 16 2008 David Walluck <walluck@mandriva.org> 0:4.2.3-1mdv2008.1
+ Revision: 153858
- use gentoo version number which includes the release in the version string

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill extra spacing at top of description

* Thu Dec 13 2007 David Walluck <walluck@mandriva.org> 0:4.2-1mdv2008.1
+ Revision: 119479
- 4.2-3

* Sat Nov 10 2007 David Walluck <walluck@mandriva.org> 0:4.1.2-1mdv2008.1
+ Revision: 107319
- change version to match gentoo

* Fri Aug 17 2007 David Walluck <walluck@mandriva.org> 0:4.1-1mdv2008.0
+ Revision: 65324
- needs desktop-file-utils
- BuildRequires: tiff-devel
- Import djview4


