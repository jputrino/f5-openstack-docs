.. _add-nova-flavors:

How to add BIG-IP VE-compatible flavors to OpenStack Nova
=========================================================

The flavor requirements for BIG-IP VE depend on the number of modules included in your `F5 BIG-IP license <https://f5.com/products/how-to-buy/simplified-licensing>`_ -- Good, Better, or Best.

.. important::

   By default, only admin users can create Nova flavors.
   See `OpenStack Horizon - Manage flavors`_ for more information.

You can add custom flavors to OpenStack Nova using the `OpenStack CLI`_.
Commands follow the format ::

   $ openstack flavor create FLAVOR_NAME --id FLAVOR_ID --ram RAM_IN_MB --disk ROOT_DISK_IN_GB --vcpus NUMBER_OF_VCPUS

\

.. note::

   The values shown here reflect the requirements for `BIG-IP Virtual Edition v13.0.0`_.

Good license
------------

The BIG-IP Good license includes the Local Traffic Manager (LTM) module with optional SDN and Advanced Routing services.

.. code-block:: console

   openstack flavor create f5.small --id auto --ram 4096 --disk 8 --vcpus 2

Better license
--------------

The BIG-IP Better license includes the LTM, `DNS`_, `Application Acceleration Manager`_ (AAM), and `Advanced Firewall Manager`_ (AFM) modules. [#AAM]_

.. code-block:: console

   openstack flavor create f5.medium --id auto --ram 8192 --disk 39 --vcpus 4

Best license
------------

The BIG-IP Best license includes everything in the Better license, plus `Application Security Manager`_ (ASM) and `Access Policy Manager`_ (APM).

.. code-block:: console

   openstack flavor create f5.large --id auto --ram 8192 --disk 149 --vcpus 4

\

.. tip::

   If you're using the BIG-IP Application Acceleration Manager (AAM) module, increase the disk size to 160.



.. rubric:: Footnotes
.. [#AAM] BIG-IP Application Acceleration Manager is not included in Better/Best on F5 BIG-IP iSeries platforms

.. _OpenStack Horizon - Manage flavors: https://docs.openstack.org/horizon/latest/admin/manage-flavors.html
.. _Local Traffic Manager: https://f5.com/products/big-ip/local-traffic-manager-ltm
.. _DNS: https://f5.com/products/big-ip/big-ip-dns
.. _Application Acceleration Manager: https://f5.com/products/big-ip/application-acceleration-manager-aam
.. _Advanced Firewall Manager: https://f5.com/products/big-ip/advanced-firewall-manager-afm
.. _BIG-IP Virtual Edition v13.0.0: https://support.f5.com/csp/article/K14946