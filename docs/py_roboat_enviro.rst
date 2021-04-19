API Reference
=============

roboat\_enviro\_backend module
-------------------------------------------------

.. autoclass:: py_roboat_enviro.roboat_enviro_backend.RoboatEnviroData
   :members:
   
   .. automethod:: get_users(self)
   .. automethod:: get_user_by_id(self, user_id)
   .. automethod:: search_users(self, filters)
   .. automethod:: add_sensor(self, nickname)
   .. automethod:: get_sensors(self)
   .. automethod:: get_sensor_by_id(self, sensor_id)
   .. automethod:: search_sensors(self, filters)
   .. automethod:: add_sensor_diagnostics(self, sensor_diagnostics)
   .. automethod:: search_sensor_diagnostics(self, filters)
   .. automethod:: add_sensor_logs(self, sensor_logs)
   .. automethod:: search_sensor_logs(self, filters)
   .. automethod:: add_gps_measurements(self, gps_measurements)
   .. automethod:: search_gps_measurements(self, filters)
   .. automethod:: add_spectroscopy_measurement_metadata(self, scan_file, metadata)
   .. automethod:: search_spectroscopy_measurement_metadata(self, filters)
   .. automethod:: get_spec_measurement_filenames(self)
   .. automethod:: get_spec_measurements_by_filename(self, filename)