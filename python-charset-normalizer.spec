Name:           python-charset-normalizer
Version:        2.0.4
Release:        1%{?dist}
Summary:        The Real First Universal Charset Detector

License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)


%description
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, trying to resolve the issue by taking
a new approach. All IANA character set names for which the Python core
library provides codecs are supported.

%package -n     python3-charset-normalizer
Summary:        %{summary}

%description -n python3-charset-normalizer
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, trying to resolve the issue by taking
a new approach. All IANA character set names for which the Python core
library provides codecs are supported.

%prep
%autosetup -n charset_normalizer-%{version}
# Remove pytest-cov settings from setup.cfg
sed -i "/addopts = --cov/d" setup.cfg

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files charset_normalizer

%check
%pytest

%files -n python3-charset-normalizer -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/normalizer

%changelog
* Mon Aug 02 2021 Lumír Balhar <lbalhar@redhat.com> - 2.0.4-1
- Update to 2.0.4
Resolves: rhbz#1988575

* Wed Jul 21 2021 Lumír Balhar <lbalhar@redhat.com> - 2.0.3-1
- Initial package
