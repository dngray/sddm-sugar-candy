%global srcname copr-sddm-sugar-candy
%global commit 2b72ef6c6f720fe0ffde5ea5c7c48152e02f6c4f
%global commitdate 20200201
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: sddm-sugar-candy
Version: 1.1^%{commitdate}.%{shortcommit}
Release: 0%{?dist}
License: GPLv3
Summary: Sugar Candy is the sweetest login theme available for the SDDM display manager.
URL: https://framagit.org/MarianArlt/%{name}
Source0: %{URL}/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch: noarch

Requires: qt5-qtgraphicaleffects
Requires: qt5-qtquickcontrols2
Requires: qt5-qtsvg
Requires: sddm

%description
You asked for more, you shall get it. Sugar Candy is the latest release in the
Sugar series of SDDM themes. It's so extremely sweet your pancreas will have
difficulties digesting its awesomeness.

Sweeten the login experience for your users, your family and yourself. Sugar
Candy works on almost all major distributions—see below—and focuses on a
straight forward user experience and superb functionality while still offering
vast customization possibilities.

Sugar Candy is based on the Sugar series which was written completely from
scratch making it clean and simple not only by looks but by design too.

All controls use the latest Qt Quick Controls 2 for increased performance on
low end or even embedded systems and beautiful color transitions.

To learn how to control sugar levels read the section below about customization.
There are 40 customizable variables in total! This candy will be yours and only
yours.

%prep
%setup -n %{name}-%{commit}

%install
mkdir -p %{buildroot}%{_datadir}/sddm/themes/sugar-candy
cp -ar {Assets,Backgrounds,Components,Main.qml,metadata.desktop} \
        %{buildroot}%{_datadir}/sddm/themes/sugar-candy
cp theme.conf %{buildroot}%{_datadir}/sddm/themes/sugar-candy/theme.conf

%files
%license COPYING
%doc AUTHORS
%doc CHANGELOG.md
%doc CREDITS
%doc README.md
%{_datadir}/sddm/themes/sugar-candy

%changelog
