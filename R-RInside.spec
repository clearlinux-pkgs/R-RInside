#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: f4a13a5
#
Name     : R-RInside
Version  : 0.2.18
Release  : 51
URL      : https://cran.r-project.org/src/contrib/RInside_0.2.18.tar.gz
Source0  : https://cran.r-project.org/src/contrib/RInside_0.2.18.tar.gz
Summary  : C++ Classes to Embed R in C++ (and C) Applications
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RInside-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R
BuildRequires : openmpi

%description
A C++ class providing the R interpreter is offered by this package
 making it easier to have "R inside" your C++ application. As R itself
 is embedded into your application, a shared library build of R is
 required. This works on Linux, OS X and even on Windows provided you
 use the same tools used to build R itself. Numerous examples are
 provided in the nine subdirectories of the examples/ directory of

%package lib
Summary: lib components for the R-RInside package.
Group: Libraries

%description lib
lib components for the R-RInside package.


%prep
%setup -q -n RInside
pushd ..
cp -a RInside buildavx2
popd
pushd ..
cp -a RInside buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1737156139

%install
export SOURCE_DATE_EPOCH=1737156139
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/RInside/DESCRIPTION
/usr/lib64/R/library/RInside/INDEX
/usr/lib64/R/library/RInside/Meta/Rd.rds
/usr/lib64/R/library/RInside/Meta/features.rds
/usr/lib64/R/library/RInside/Meta/hsearch.rds
/usr/lib64/R/library/RInside/Meta/links.rds
/usr/lib64/R/library/RInside/Meta/nsInfo.rds
/usr/lib64/R/library/RInside/Meta/package.rds
/usr/lib64/R/library/RInside/NAMESPACE
/usr/lib64/R/library/RInside/NEWS.Rd
/usr/lib64/R/library/RInside/R/RInside
/usr/lib64/R/library/RInside/R/RInside.rdb
/usr/lib64/R/library/RInside/R/RInside.rdx
/usr/lib64/R/library/RInside/THANKS
/usr/lib64/R/library/RInside/examples/armadillo/GNUmakefile
/usr/lib64/R/library/RInside/examples/armadillo/cmake/CMakeLists.txt
/usr/lib64/R/library/RInside/examples/armadillo/cmake/WIN.readme.txt
/usr/lib64/R/library/RInside/examples/armadillo/rinside_arma0.cpp
/usr/lib64/R/library/RInside/examples/armadillo/rinside_arma1.cpp
/usr/lib64/R/library/RInside/examples/c_interface/GNUmakefile
/usr/lib64/R/library/RInside/examples/c_interface/hello.c
/usr/lib64/R/library/RInside/examples/c_interface/hello.rb
/usr/lib64/R/library/RInside/examples/c_interface/passdata.c
/usr/lib64/R/library/RInside/examples/c_interface/passdata.rb
/usr/lib64/R/library/RInside/examples/eigen/GNUmakefile
/usr/lib64/R/library/RInside/examples/eigen/cmake/CMakeLists.txt
/usr/lib64/R/library/RInside/examples/eigen/cmake/WIN.readme.txt
/usr/lib64/R/library/RInside/examples/eigen/rinside_eigen0.cpp
/usr/lib64/R/library/RInside/examples/eigen/rinside_eigen1.cpp
/usr/lib64/R/library/RInside/examples/mpi/GNUmakefile
/usr/lib64/R/library/RInside/examples/mpi/cmake/CMakeLists.txt
/usr/lib64/R/library/RInside/examples/mpi/rinside_mpi_sample0.cpp
/usr/lib64/R/library/RInside/examples/mpi/rinside_mpi_sample1.cpp
/usr/lib64/R/library/RInside/examples/mpi/rinside_mpi_sample2.cpp
/usr/lib64/R/library/RInside/examples/mpi/rinside_mpi_sample3.cpp
/usr/lib64/R/library/RInside/examples/mpi/rinside_mpi_sample4.cpp
/usr/lib64/R/library/RInside/examples/qt/README
/usr/lib64/R/library/RInside/examples/qt/cmake/CMakeLists.txt
/usr/lib64/R/library/RInside/examples/qt/main.cpp
/usr/lib64/R/library/RInside/examples/qt/qtdensity.cpp
/usr/lib64/R/library/RInside/examples/qt/qtdensity.h
/usr/lib64/R/library/RInside/examples/qt/qtdensity.pro
/usr/lib64/R/library/RInside/examples/sandboxed_server/GNUmakefile
/usr/lib64/R/library/RInside/examples/sandboxed_server/client/callback_helper.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/client/rinsideclient.cpp
/usr/lib64/R/library/RInside/examples/sandboxed_server/client/rinsideclient.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/common/binarystream.cpp
/usr/lib64/R/library/RInside/examples/sandboxed_server/common/binarystream.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/common/constants.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/common/typeid.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/datatypes/bar.cpp
/usr/lib64/R/library/RInside/examples/sandboxed_server/datatypes/bar.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/datatypes/bar_rcpp_wrapper_declarations.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/datatypes/bar_rcpp_wrapper_definitions.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/datatypes/foo.cpp
/usr/lib64/R/library/RInside/examples/sandboxed_server/datatypes/foo.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/datatypes/foo_rcpp_wrapper_declarations.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/datatypes/foo_rcpp_wrapper_definitions.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/example_client.cpp
/usr/lib64/R/library/RInside/examples/sandboxed_server/example_server.cpp
/usr/lib64/R/library/RInside/examples/sandboxed_server/server/internalfunction_clone.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/server/rinside_callbacks.h
/usr/lib64/R/library/RInside/examples/sandboxed_server/server/rinsideserver.cpp
/usr/lib64/R/library/RInside/examples/sandboxed_server/server/rinsideserver.h
/usr/lib64/R/library/RInside/examples/standard/GNUmakefile
/usr/lib64/R/library/RInside/examples/standard/Makefile.win
/usr/lib64/R/library/RInside/examples/standard/cmake/CMakeLists.txt
/usr/lib64/R/library/RInside/examples/standard/rinside_callbacks0.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_callbacks1.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_interactive0.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_module_sample0.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample0.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample1.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample10.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample11.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample12.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample13.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample14.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample15.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample16.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample17.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample2.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample3.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample4.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample5.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample6.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample7.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample8.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_sample9.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_test0.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_test1.cpp
/usr/lib64/R/library/RInside/examples/standard/rinside_test2.cpp
/usr/lib64/R/library/RInside/examples/threads/GNUmakefile
/usr/lib64/R/library/RInside/examples/threads/boostEx.cpp
/usr/lib64/R/library/RInside/examples/wt/GNUmakefile
/usr/lib64/R/library/RInside/examples/wt/cmake/CMakeLists.txt
/usr/lib64/R/library/RInside/examples/wt/wtdensity.cpp
/usr/lib64/R/library/RInside/examples/wt/wtdensity.css
/usr/lib64/R/library/RInside/examples/wt/wtdensity.xml
/usr/lib64/R/library/RInside/examples/wt/wtdensityPlain.cpp
/usr/lib64/R/library/RInside/help/AnIndex
/usr/lib64/R/library/RInside/help/RInside.rdb
/usr/lib64/R/library/RInside/help/RInside.rdx
/usr/lib64/R/library/RInside/help/aliases.rds
/usr/lib64/R/library/RInside/help/paths.rds
/usr/lib64/R/library/RInside/html/00Index.html
/usr/lib64/R/library/RInside/html/R.css
/usr/lib64/R/library/RInside/include/Callbacks.h
/usr/lib64/R/library/RInside/include/MemBuf.h
/usr/lib64/R/library/RInside/include/RInside.h
/usr/lib64/R/library/RInside/include/RInsideCommon.h
/usr/lib64/R/library/RInside/include/RInsideConfig.h
/usr/lib64/R/library/RInside/include/RInside_C.h
/usr/lib64/R/library/RInside/lib/libRInside.a

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/RInside/lib/libRInside.so
/V3/usr/lib64/R/library/RInside/libs/RInside.so
/V4/usr/lib64/R/library/RInside/lib/libRInside.so
/V4/usr/lib64/R/library/RInside/libs/RInside.so
/usr/lib64/R/library/RInside/lib/libRInside.so
/usr/lib64/R/library/RInside/libs/RInside.so
