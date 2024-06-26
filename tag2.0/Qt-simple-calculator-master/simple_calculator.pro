#-------------------------------------------------
#
# Project created by QtCreator 2017-11-03T23:09:46
#
#-------------------------------------------------

QT       += core gui

CONFIG += c++11

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = simple_calculator
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += \
        main.cpp \
        mainwindow.cpp

HEADERS += \
        mainwindow.h

FORMS += \
        mainwindow.ui

DISTFILES += \
    ../build-simple_calculator-Desktop_Qt_5_14_2_MinGW_64_bit-Debug/debug/asin.py \
    ../build-simple_calculator-Desktop_Qt_5_14_2_MinGW_64_bit-Debug/debug/atan.py \
    ../build-simple_calculator-Desktop_Qt_5_14_2_MinGW_64_bit-Debug/debug/constant.py \
    ../build-simple_calculator-Desktop_Qt_5_14_2_MinGW_64_bit-Debug/debug/cos.py \
    ../build-simple_calculator-Desktop_Qt_5_14_2_MinGW_64_bit-Debug/debug/sin.py



INCLUDEPATH += -I D:\software\python\include
LIBS += -LD:\software\python\libs -lpython312

