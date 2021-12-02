#! /usr/bin/python3

import rospy
import sys

from proteus.language import Language

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    rospy.init_node('proteus_language_server', anonymous=True)
    rospy.loginfo('Initializing the PROTEUS language server.')
        
    if not rospy.has_param('language_definition_file'):
        rospy.logerr("You need to provide a lang_def_file in the \"proteus_language_server\" parameter, should be in the launchfile.")
        sys.exit()

    lang_def_file = rospy.get_param('language_definition_file')
    rospy.loginfo("Language defintion file:%s"%lang_def_file)

    # Parse language definition file
    rospy.loginfo('Parsing language definition file...')
    tree = ET.parse(lang_def_file)
    root = tree.getroot()
    lang = Language()
    lang.parse_from_xml(root)
    
    
    rospy.loginfo('Putting symbol info on the parameter server...')
    # Put language symbols up on the ROS parameter server
    for symbol in lang.in_symbols:
        symbol_dict = {"call_type":symbol.call_type}
        rospy.set_param("symbols/in/%s"%(symbol.id), symbol_dict)

    for symbol in lang.out_symbols:
        symbol_dict = {"call_type":symbol.call_type}
        rospy.set_param("symbols/out/%s"%(symbol.id), symbol_dict)

    rospy.loginfo('Putting vector info on the parameter server...')
    # Put up vector information on the ROS parameter server
    for vector in lang.in_vectors:
        vector_dict = {"definition_file":vector.definition_file, "type":vector.type}
        rospy.set_param("vectors/in/%s"%(vector.name), vector_dict)

    for vector in lang.out_vectors:
        vector_dict = {"definition_file":vector.definition_file, "type":vector.type}
        rospy.set_param("vectors/out/%s"%(vector.name), vector_dict)

    # TODO Also put up other information as necessary



    rospy.loginfo('Language server initialized, ready for business!')
    # Time to spin forever
    r = rospy.Rate(10)
    while not rospy.is_shutdown():
        r.sleep()

else:
    print('This is a ROS node why are you trying to import it please stop.')