%global package_speccommit d2435ce0c6269090964e333a98d73f3c06ccd0ca
%global usver 2.1.0
%global xsver 4
%global xsrel %{xsver}.1%{?xscount}%{?xshash}
Name:           python-charset-normalizer
Version:        2.1.0
Release: %{?xsrel}%{?dist}
Summary:        The Real First Universal Charset Detector

License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source0: 2.1.0.tar.gz
Source1: pyproject_wheel.py
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%if 0%{?xenserver} < 9
BuildRequires:  python3-wheel
%else
BuildRequires:  python3dist(pytest)
%endif


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

%if 0%{?xenserver} >= 9
%generate_buildrequires
%pyproject_buildrequires -r
%endif

%build
%if 0%{?xenserver} < 9
echo "from setuptools import setup

setup(name=\"%{name}\",
      version='%{version}',
     )" > ./setup.py
/usr/bin/python3 -Bs %{SOURCE1} %{_builddir}/charset_normalizer-%{version}/pyproject-wheeldir
%else
%pyproject_wheel
%endif

%install
%if 0%{?xenserver} < 9
/usr/bin/python3 -m pip install --root %{buildroot} --prefix /usr --no-deps --disable-pip-version-check --verbose --ignore-installed --no-index --no-cache-dir --find-links %{_builddir}/charset_normalizer-%{version}/pyproject-wheeldir
%else
%pyproject_install
%pyproject_save_files charset_normalizer
%endif

%if 0%{?xenserver} < 9
# Copy source files to buildroot manually
mkdir -p %{buildroot}%{python3_sitelib}/charset_normalizer
cp -r %{_builddir}/charset_normalizer-%{version}/charset_normalizer %{buildroot}%{python3_sitelib}/
find %{buildroot}%{python3_sitelib}/charset_normalizer
%endif

%if 0%{?xenserver} >= 9
%check
%pytest
%endif

%if 0%{?xenserver} < 9
%files -n python3-charset-normalizer
%dir %{python3_sitelib}/charset_normalizer
%dir %{python3_sitelib}/charset_normalizer/__pycache__
%dir %{python3_sitelib}/charset_normalizer/assets
%dir %{python3_sitelib}/charset_normalizer/assets/__pycache__
%dir %{python3_sitelib}/charset_normalizer/cli
%dir %{python3_sitelib}/charset_normalizer/cli/__pycache__
%{python3_sitelib}/charset_normalizer/__init__.py
%{python3_sitelib}/charset_normalizer/__pycache__/__init__.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/__pycache__/api.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/__pycache__/cd.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/__pycache__/constant.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/__pycache__/legacy.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/__pycache__/md.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/__pycache__/models.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/__pycache__/utils.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/__pycache__/version.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/api.py
%{python3_sitelib}/charset_normalizer/assets/__init__.py
%{python3_sitelib}/charset_normalizer/assets/__pycache__/__init__.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/cd.py
%{python3_sitelib}/charset_normalizer/cli/__init__.py
%{python3_sitelib}/charset_normalizer/cli/__pycache__/__init__.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/cli/__pycache__/normalizer.cpython-*.pyc
%{python3_sitelib}/charset_normalizer/cli/normalizer.py
%{python3_sitelib}/charset_normalizer/constant.py
%{python3_sitelib}/charset_normalizer/legacy.py
%{python3_sitelib}/charset_normalizer/md.py
%{python3_sitelib}/charset_normalizer/models.py
%{python3_sitelib}/charset_normalizer/py.typed
%{python3_sitelib}/charset_normalizer/utils.py
%{python3_sitelib}/charset_normalizer/version.py
%else
%files -n python3-charset-normalizer -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/normalizer
%endif

%changelog
* Fri Jan 24 2025 Yann Dirson <yann.dirson@vates.tech> - 2.1.0-4.1
- Fix build invocation using hardcoded (and buggy) paths

* Mon Aug 19 2024 Marcus Granado <marcus.granado@cloud.com> - 2.1.0-4
- Bump release and rebuild

* Fri Aug 09 2024 Marcus Granado <marcus.granado@cloud.com> - 2.1.0-3
- Bump release and rebuild

* Fri Jul 07 2023 Tim Smith <tim.smith@citrix.com> - 2.1.0-1
- First imported release

