Name:           djview4
Version:        4.5
Release:        %mkrel 2
Epoch:          0
Summary:        DjVu viewer and browser plugin
License:        GPLv2+
Group:          Publishing
URL:            http://djvu.sourceforge.net/djview4.html
Source0:        http://downloads.sourceforge.net/djvu/%{name}-%{version}.tar.gz
Patch0:		djview4-4.5-mdv-fix-str-fmt.patch
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
BuildRequires:  desktop-file-utils
BuildRequires:  djvulibre-devel
BuildRequires:  qt4-devel
BuildRequires:  tiff-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
This package contains the djview4 viewer and browser plugin.
This new viewer relies on the DjVulibre library and the Qt4 toolkit.

Highlights:

- entirely based on the public djvulibre api.
- entirely written in portable Qt4.
- has been reported to work with Qt/Mac.
- should work with Qt/Windows as well.
- continuous scrolling of pages
- side-by-side display of pages
- ability to specify a url to the djview command
- all plugin and cgi options available from the command line
- all silly annotations implemented
- display thumbnails as a grid
- display outlines
- page names supported (see djvused command set-page-title)
- metadata dialog (see djvused command set-meta)
- implemented as reusable Qt widgets

%package -n mozilla-plugin-dejavu
Summary:        UNIX-based DjVu Netscape plugin
Group:          Publishing
Requires:       %{name} = %{epoch}:%{version}-%{release}
Obsoletes:      djvulibre-browser-plugin < %{epoch}:%{version}-%{release}
Provides:       djvulibre-browser-plugin = %{epoch}:%{version}-%{release}

%description -n mozilla-plugin-dejavu
UNIX-based DjVu Netscape plugin.

%prep
%setup -q -n djview4-%{version}
%patch0 -p1 -b .strfmt

%build
export QTDIR=%{qt4dir}
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}
%{__rm} -r %{buildroot}%{_datadir}/djvu/djview4/desktop
%if 0
%{__rm} %{buildroot}%{_bindir}/djview
%{__rm} %{buildroot}%{_mandir}/man1/djview.1
%endif
%{__mkdir_p} %{buildroot}%{_libdir}/mozilla/plugins
%{__mv} %{buildroot}%{_libdir}/netscape/plugins/nsdejavu.so %{buildroot}%{_libdir}/mozilla/plugins/nsdejavu.so
%{__ln_s} %{_libdir}/mozilla/plugins/nsdejavu.so %{buildroot}%{_libdir}/netscape/plugins/nsdejavu.so

%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
%{__cp} -a desktopfiles/hi32-djview4.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/djvulibre-djview4.png
%{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
%{__cp} -a desktopfiles/hi64-djview4.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/djvulibre-djview4.png
%{_bindir}/desktop-file-install \
  --vendor="" \
  --remove-category="Application" \
  --add-category="Qt" \
  --add-category="Graphics" \
  --add-category="Viewer" \
  --dir %{buildroot}%{_datadir}/applications desktopfiles/djvulibre-djview4.desktop

%post
%update_icon_cache hicolor
%{update_mime_database}
%{update_desktop_database}

%postun
%clean_icon_cache hicolor
%{clean_mime_database}
%{clean_desktop_database}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc COPYING COPYRIGHT INSTALL NEWS README README_packagers README_translations TODO
%attr(0755,root,root) %{_bindir}/djview
%attr(0755,root,root) %{_bindir}/djview4
%{_datadir}/djvu/djview4/
%{_mandir}/man1/djview4.1*
%{_mandir}/man1/djview.1*
%{_datadir}/applications/djvulibre-djview4.desktop
%{_datadir}/icons/hicolor/*/apps/djvulibre-djview4.png

%files -n mozilla-plugin-dejavu
%defattr(0644,root,root,0755)
%doc nsdejavu/README
%attr(0755,root,root) %{_libdir}/netscape/plugins/nsdejavu.so
%attr(0755,root,root) %{_libdir}/mozilla/plugins/nsdejavu.so
%{_mandir}/man1/nsdejavu.1*
