import QtQuick
import QtPositioning
import QtLocation
import QtQuick.Controls

Item
{
    id: root
    visible: true

    Plugin
    {
        id: osmPlug
        name: "osm"

        PluginParameter
        {
            name: "osm.mapping.providersrepository.disabled"
            value: "true"
        }
        PluginParameter
        {
            name: "osm.mapping.providersrepository.address"
            value: "http://maps-redirect.qt.io/osm/5.6/"
        }
    }

    Map
    {
        id: map
        anchors.fill: parent
        plugin: osmPlug
        center: QtPositioning.coordinate(34.0597, -4.9653)
        zoomLevel: 3
        copyrightsVisible: false
        fieldOfView: 15

        MapQuickItem {
            coordinate: QtPositioning.coordinate(34.0597, -4.9653)

            anchorPoint.x: marker.width / 2
            anchorPoint.y: marker.height / 2

            sourceItem: Rectangle {
                id: marker
                width: 14
                height: 14
                radius: 7
                color: "red"
                border.color: "white"
                border.width: 2
            }
        }
    }
Column {
    anchors.right: parent.right
    anchors.bottom: parent.bottom
    anchors.rightMargin: 20
    anchors.bottomMargin: 20
    spacing: 10

    Button {
        text: "+"
        width: 40
        height: 40
        onClicked: map.zoomLevel += 1
    }

    Button {
        text: "-"
        width: 40
        height: 40
        onClicked: map.zoomLevel -= 1
    }
}
}
