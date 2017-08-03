%global srcname stringprep


Name: erlang-%{srcname}
Version: 1.0.6
Release: %mkrel 1

Group:   Development/Erlang
License: ASL 2.0 and TCL
Summary: A framework for preparing Unicode strings to help input and comparison
URL: https://github.com/processone/stringprep/
Source0: https://github.com/processone/stringprep/archive/%{version}.tar.gz

Provides:  erlang-p1_stringprep = %{version}-%{release}
Obsoletes: erlang-p1_stringprep < 1.0.3

BuildRequires: erlang-rebar
BuildRequires: erlang-p1_utils >= 1.0.5

%{?__erlang_nif_version:Requires: %{__erlang_nif_version}}


%description
Stringprep is a framework for preparing Unicode test strings in order to
increase the likelihood that string input and string comparison work. The
principle are defined in RFC-3454: Preparation of Internationalized Strings.
This library is leverage Erlang native NIF mechanism to provide extremely fast
and efficient processing.


%prep
%autosetup -n stringprep-%{version}


%build
%{rebar_compile}


%install
install -d $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib

install -pm755 priv/lib/* $RPM_BUILD_ROOT%{_erllibdir}/%{srcname}-%{version}/priv/lib/
%{erlang_install}


%check
%{rebar_eunit}


%files
%license LICENSE.txt LICENSE.TCL LICENSE.ALL
%doc README.md
%{erlang_appdir}



%changelog
* Thu Nov 17 2016 neoclust <neoclust> 1.0.6-1.mga6
+ Revision: 1067974
- imported package erlang-stringprep

