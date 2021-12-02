#! /usr/bin/python3

import rospy
import sys

from proteus.language import Language

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    rospy.init_node('proteus_language_server', anonymous=True)
        
    if not rospy.has_param('language_definition_file'):
        rospy.logerr("You need to provide a lang_def_file in the \"proteus_language_server\" parameter, should be in the launchfile.")
        sys.exit()

    lang_def_file = rospy.get_param('language_definition_file')
    rospy.loginfo("Language defintion:%s"%lang_def_file)

    tree = ET.parse(lang_def_file)
    root = tree.getroot()

    # Parse language definition file
    lang = Language()
    lang.parse_from_xml(root)
    
    # Put language symbols up on the ROS parameter server
    # TODO Also put up other information as necessary

    
    for symbol in lang.in_symbols:
        pass

    for symbol in lang.out_symbols:
        symbol_dict = {"call_type":symbol.call_type}
        rospy.set_param("symbols/out/%s"%(symbol.id), symbol_dict)


    # Time to spin forever
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        r.sleep()

else:
    print('This is a ROS node why are you trying to import it please stop.')