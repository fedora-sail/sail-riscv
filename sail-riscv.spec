Name:           sail-riscv
Version:        master
Release:        %autorelease
Summary:        Sail RISC-V model

License:        Sail
URL:            https://github.com/riscv/%{name}
Source0:        https://github.com/riscv/%{name}/archive/refs/heads/%{version}.zip

BuildRequires:  lem-devel
BuildRequires:  linksem-devel
BuildRequires:  sail-devel
BuildRequires:  zlib-devel
BuildRequires:  z3
BuildRequires:  opam
BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ocamlbuild

%description
The model specifies assembly language formats of the instructions, the corresponding encoders and decoders, and the instruction semantics. The current status of its coverage of the prose RISC-V specification is summarized here. A reading guide to the model is provided in the doc/ subdirectory, along with a guide on how to extend the model.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version} -p1
sed -i 's|SAIL:=$(SAIL_DIR)/sail|SAIL:=/usr/bin/sail|' Makefile

%build
# %make_build SAIL_DIR=/usr/share/sail
ARCH=64 make c_emulator/riscv_sim_RV64 SAIL_DIR=/usr/share/sail
ARCH=32 make c_emulator/riscv_sim_RV32 SAIL_DIR=/usr/share/sail

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datarootdir}
cp c_emulator/riscv_sim_RV* %{buildroot}/%{_bindir}/
cp -r model %{buildroot}/%{_datarootdir}/sail-riscv
# %make_install

%check
# %make_check

%files
%license LICENCE
%doc README.md
%{_bindir}/*

%files devel
%dir %{_datadir}/sail-riscv
%{_datadir}/sail-riscv/*

%changelog
%autochangelog
