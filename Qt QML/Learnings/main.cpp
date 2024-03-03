#include <QGuiApplication>
#include <QQmlApplicationEngine>
#include <QtQuick>

int main(int argc, char *argv[])
{
    QGuiApplication app(argc, argv);
    QQuickView view;
    view.setSource(QUrl(u"qrc:/Learnings/Main.qml"_qs));
    view.show();
    // QQmlApplicationEngine engine;
    // const QUrl url(u"qrc:/Learnings/Main.qml"_qs);
    // QObject::connect(
    //     &engine,
    //     &QQmlApplicationEngine::objectCreationFailed,
    //     &app,
    //     []() { QCoreApplication::exit(-1); },
    //     Qt::QueuedConnection);
    // engine.load(url);

    return app.exec();
}
