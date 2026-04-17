# UNIVERSAL KUBERNETES DEPLOYMENT TEMPLATES

## Overview

This document provides **MANDATORY** universal Kubernetes deployment templates that follow KISS principles, industry best practices, and strict compliance with the `MANDATORY-DEPLOYMENT-STRUCTURE.md`. These templates are production-ready and universally deployable across all supported platforms.

## Template Categories

### 1. Microservice Template
### 2. Web Application Template  
### 3. Database Service Template
### 4. Worker Service Template
### 5. API Gateway Template

---

## 1. MICROSERVICE TEMPLATE

### Directory Structure
```
k8s/apps/microservice-template/
├── base/
│   ├── kustomization.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   ├── ingress.yaml
│   └── hpa.yaml
├── overlays/
│   ├── development/
│   │   ├── kustomization.yaml
│   │   ├── replica-patch.yaml
│   │   ├── resource-patch.yaml
│   │   └── env-vars.yaml
│   ├── staging/
│   │   ├── kustomization.yaml
│   │   ├── replica-patch.yaml
│   │   ├── resource-patch.yaml
│   │   └── env-vars.yaml
│   └── production/
│       ├── kustomization.yaml
│       ├── replica-patch.yaml
│       ├── resource-patch.yaml
│       ├── env-vars.yaml
│       └── pdb.yaml
├── configs/
│   ├── app-config.yaml
│   ├── logging-config.yaml
│   └── monitoring-config.yaml
├── secrets/
│   ├── secret-template.yaml
│   ├── external-secret.yaml
│   └── sealed-secret.yaml
├── policies/
│   ├── network-policy.yaml
│   ├── pod-security-policy.yaml
│   └── resource-quota.yaml
├── tests/
│   ├── health-check.yaml
│   ├── integration-test.yaml
│   └── smoke-test.yaml
├── monitoring/
│   ├── servicemonitor.yaml
│   ├── prometheusrule.yaml
│   └── grafana-dashboard.json
└── docs/
    ├── README.md
    ├── DEPLOYMENT.md
    ├── TROUBLESHOOTING.md
    └── API.md
```

### Base Templates

#### base/kustomization.yaml
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

metadata:
  name: microservice-base
  annotations:
    config.kubernetes.io/local-config: "true"

resources:
- deployment.yaml
- service.yaml
- configmap.yaml
- ingress.yaml
- hpa.yaml

commonLabels:
  app.kubernetes.io/name: microservice-template
  app.kubernetes.io/component: backend
  app.kubernetes.io/part-of: platform

commonAnnotations:
  app.kubernetes.io/managed-by: kustomize
  deployment.kubernetes.io/created-by: universal-k8s-deployment

images:
- name: microservice
  newName: registry.example.com/microservice
  newTag: latest

replicas:
- name: microservice-deployment
  count: 3

namespace: default
```

#### base/deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: microservice-deployment
  labels:
    app.kubernetes.io/name: microservice-template
    app.kubernetes.io/version: "1.0.0"
    app.kubernetes.io/component: backend
    app.kubernetes.io/part-of: platform
    app.kubernetes.io/managed-by: kustomize
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app.kubernetes.io/name: microservice-template
      app.kubernetes.io/component: backend
  template:
    metadata:
      labels:
        app.kubernetes.io/name: microservice-template
        app.kubernetes.io/version: "1.0.0"
        app.kubernetes.io/component: backend
        app.kubernetes.io/part-of: platform
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
        prometheus.io/path: "/metrics"
    spec:
      serviceAccountName: microservice-sa
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        runAsGroup: 3000
        fsGroup: 2000
        seccompProfile:
          type: RuntimeDefault
      containers:
      - name: microservice
        image: microservice:latest
        ports:
        - name: http
          containerPort: 8080
          protocol: TCP
        - name: metrics
          containerPort: 9090
          protocol: TCP
        env:
        - name: PORT
          value: "8080"
        - name: ENVIRONMENT
          value: "production"
        - name: LOG_LEVEL
          value: "info"
        envFrom:
        - configMapRef:
            name: microservice-config
        - secretRef:
            name: microservice-secrets
        resources:
          requests:
            memory: "128Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "200m"
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          runAsNonRoot: true
          runAsUser: 1000
          capabilities:
            drop:
            - ALL
        livenessProbe:
          httpGet:
            path: /health
            port: http
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          successThreshold: 1
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /ready
            port: http
          initialDelaySeconds: 5
          periodSeconds: 5
          timeoutSeconds: 3
          successThreshold: 1
          failureThreshold: 3
        startupProbe:
          httpGet:
            path: /startup
            port: http
          initialDelaySeconds: 10
          periodSeconds: 5
          timeoutSeconds: 3
          successThreshold: 1
          failureThreshold: 10
        volumeMounts:
        - name: tmp
          mountPath: /tmp
        - name: var-run
          mountPath: /var/run
        - name: config-volume
          mountPath: /etc/config
          readOnly: true
      volumes:
      - name: tmp
        emptyDir: {}
      - name: var-run
        emptyDir: {}
      - name: config-volume
        configMap:
          name: microservice-config
      terminationGracePeriodSeconds: 30
      restartPolicy: Always
```

#### base/service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: microservice-service
  labels:
    app.kubernetes.io/name: microservice-template
    app.kubernetes.io/component: backend
    app.kubernetes.io/part-of: platform
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: nlb
    service.beta.kubernetes.io/azure-load-balancer-resource-group: k8s-rg
spec:
  type: ClusterIP
  selector:
    app.kubernetes.io/name: microservice-template
    app.kubernetes.io/component: backend
  ports:
  - name: http
    port: 80
    targetPort: http
    protocol: TCP
  - name: metrics
    port: 9090
    targetPort: metrics
    protocol: TCP
  sessionAffinity: None
```

#### base/configmap.yaml
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: microservice-config
  labels:
    app.kubernetes.io/name: microservice-template
    app.kubernetes.io/component: configuration
data:
  # Application configuration
  app.properties: |
    server.port=8080
    server.shutdown=graceful
    spring.application.name=microservice-template
    logging.level.com.example=INFO
    management.endpoints.web.exposure.include=health,ready,metrics,prometheus
    management.endpoint.health.show-details=when-authorized
    management.metrics.export.prometheus.enabled=true
    
  # Logging configuration
  logging.yaml: |
    logging:
      level:
        root: INFO
        com.example: INFO
      pattern:
        console: "%d{yyyy-MM-dd HH:mm:ss} - %msg%n"
        file: "%d{yyyy-MM-dd HH:mm:ss} [%thread] %-5level %logger{36} - %msg%n"
      file:
        name: /var/log/app.log
        max-size: 10MB
        max-history: 5
        
  # Monitoring configuration
  monitoring.yaml: |
    metrics:
      enabled: true
      port: 9090
      path: /metrics
    tracing:
      enabled: true
      sampling-rate: 0.1
    health:
      checks:
        database: true
        redis: true
        external-api: true
```

#### base/ingress.yaml
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: microservice-ingress
  labels:
    app.kubernetes.io/name: microservice-template
    app.kubernetes.io/component: ingress
  annotations:
    # NGINX Ingress Controller
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
    
    # AWS Load Balancer Controller
    kubernetes.io/ingress.class: alb
    alb.ingress.kubernetes.io/scheme: internet-facing
    alb.ingress.kubernetes.io/target-type: ip
    alb.ingress.kubernetes.io/backend-protocol: HTTP
    alb.ingress.kubernetes.io/healthcheck-path: /health
    
    # Azure Application Gateway
    kubernetes.io/ingress.class: azure/application-gateway
    appgw.ingress.kubernetes.io/backend-path-prefix: /
    
    # GCP Load Balancer
    kubernetes.io/ingress.class: gce
    cloud.google.com/backend-config: '{"default": "microservice-backendconfig"}'
    
    # Certificate management
    cert-manager.io/cluster-issuer: letsencrypt-prod
    
    # Security headers
    nginx.ingress.kubernetes.io/configuration-snippet: |
      add_header X-Content-Type-Options nosniff;
      add_header X-Frame-Options DENY;
      add_header X-XSS-Protection "1; mode=block";
      add_header Strict-Transport-Security "max-age=31536000; includeSubDomains";
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - api.example.com
    secretName: microservice-tls
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /api/v1
        pathType: Prefix
        backend:
          service:
            name: microservice-service
            port:
              number: 80
```

#### base/hpa.yaml
```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: microservice-hpa
  labels:
    app.kubernetes.io/name: microservice-template
    app.kubernetes.io/component: autoscaling
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: microservice-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  - type: Pods
    pods:
      metric:
        name: custom_requests_per_second
      target:
        type: AverageValue
        averageValue: "100"
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Percent
        value: 10
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
      - type: Percent
        value: 50
        periodSeconds: 30
      - type: Pods
        value: 2
        periodSeconds: 60
      selectPolicy: Max
```

### Environment Overlays

#### overlays/development/kustomization.yaml
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: development

resources:
- ../../base

patchesStrategicMerge:
- replica-patch.yaml
- resource-patch.yaml
- env-vars.yaml

images:
- name: microservice
  newTag: dev-latest

commonLabels:
  environment: development

commonAnnotations:
  deployment.environment: development
  deployment.tier: non-production
```

#### overlays/development/replica-patch.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: microservice-deployment
spec:
  replicas: 1
```

#### overlays/development/resource-patch.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: microservice-deployment
spec:
  template:
    spec:
      containers:
      - name: microservice
        resources:
          requests:
            memory: "64Mi"
            cpu: "50m"
          limits:
            memory: "128Mi"
            cpu: "100m"
```

#### overlays/development/env-vars.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: microservice-deployment
spec:
  template:
    spec:
      containers:
      - name: microservice
        env:
        - name: ENVIRONMENT
          value: "development"
        - name: LOG_LEVEL
          value: "debug"
        - name: DATABASE_URL
          value: "postgresql://localhost:5432/myapp_dev"
```

#### overlays/staging/kustomization.yaml
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: staging

resources:
- ../../base

patchesStrategicMerge:
- replica-patch.yaml
- resource-patch.yaml
- env-vars.yaml

images:
- name: microservice
  newTag: staging-latest

commonLabels:
  environment: staging

commonAnnotations:
  deployment.environment: staging
  deployment.tier: non-production
```

#### overlays/staging/replica-patch.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: microservice-deployment
spec:
  replicas: 2
```

#### overlays/production/kustomization.yaml
```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

namespace: production

resources:
- ../../base
- pdb.yaml

patchesStrategicMerge:
- replica-patch.yaml
- resource-patch.yaml
- env-vars.yaml

images:
- name: microservice
  newTag: v1.0.0

commonLabels:
  environment: production

commonAnnotations:
  deployment.environment: production
  deployment.tier: production
```

#### overlays/production/pdb.yaml
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: microservice-pdb
  labels:
    app.kubernetes.io/name: microservice-template
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app.kubernetes.io/name: microservice-template
      app.kubernetes.io/component: backend
```

### Security Policies

#### policies/network-policy.yaml
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: microservice-network-policy
  labels:
    app.kubernetes.io/name: microservice-template
spec:
  podSelector:
    matchLabels:
      app.kubernetes.io/name: microservice-template
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: ingress-nginx
    - namespaceSelector:
        matchLabels:
          name: monitoring
    - podSelector:
        matchLabels:
          app.kubernetes.io/name: api-gateway
    ports:
    - protocol: TCP
      port: 8080
    - protocol: TCP
      port: 9090
  egress:
  - to:
    - podSelector:
        matchLabels:
          app.kubernetes.io/name: database
    ports:
    - protocol: TCP
      port: 5432
  - to:
    - podSelector:
        matchLabels:
          app.kubernetes.io/name: redis
    ports:
    - protocol: TCP
      port: 6379
  - to: []
    ports:
    - protocol: UDP
      port: 53
    - protocol: TCP
      port: 53
  - to: []
    ports:
    - protocol: TCP
      port: 443
    - protocol: TCP
      port: 80
```

#### policies/pod-security-policy.yaml
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: microservice-namespace
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
    app.kubernetes.io/name: microservice-template

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: microservice-sa
  namespace: microservice-namespace
  labels:
    app.kubernetes.io/name: microservice-template
automountServiceAccountToken: false

---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: microservice-namespace
  name: microservice-role
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list", "watch"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: microservice-rolebinding
  namespace: microservice-namespace
subjects:
- kind: ServiceAccount
  name: microservice-sa
  namespace: microservice-namespace
roleRef:
  kind: Role
  name: microservice-role
  apiGroup: rbac.authorization.k8s.io
```

### Monitoring Configuration

#### monitoring/servicemonitor.yaml
```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: microservice-servicemonitor
  labels:
    app.kubernetes.io/name: microservice-template
    app.kubernetes.io/component: monitoring
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: microservice-template
  endpoints:
  - port: metrics
    interval: 30s
    path: /metrics
    scrapeTimeout: 10s
    honorLabels: true
    relabelings:
    - sourceLabels: [__meta_kubernetes_pod_name]
      targetLabel: instance
    - sourceLabels: [__meta_kubernetes_pod_node_name]
      targetLabel: node
```

#### monitoring/prometheusrule.yaml
```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: microservice-alerts
  labels:
    app.kubernetes.io/name: microservice-template
    app.kubernetes.io/component: monitoring
spec:
  groups:
  - name: microservice.rules
    rules:
    - alert: MicroserviceDown
      expr: up{job="microservice-template"} == 0
      for: 5m
      labels:
        severity: critical
        service: microservice-template
      annotations:
        summary: "Microservice instance is down"
        description: "Microservice {{ $labels.instance }} has been down for more than 5 minutes."
        
    - alert: MicroserviceHighErrorRate
      expr: rate(http_requests_total{job="microservice-template",status=~"5.."}[5m]) > 0.1
      for: 5m
      labels:
        severity: warning
        service: microservice-template
      annotations:
        summary: "High error rate detected"
        description: "Error rate is {{ $value }} errors per second for {{ $labels.instance }}."
        
    - alert: MicroserviceHighLatency
      expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{job="microservice-template"}[5m])) > 0.5
      for: 10m
      labels:
        severity: warning
        service: microservice-template
      annotations:
        summary: "High latency detected"
        description: "95th percentile latency is {{ $value }} seconds for {{ $labels.instance }}."
        
    - alert: MicroserviceHighMemoryUsage
      expr: container_memory_usage_bytes{container="microservice"} / container_spec_memory_limit_bytes * 100 > 90
      for: 10m
      labels:
        severity: warning
        service: microservice-template
      annotations:
        summary: "High memory usage"
        description: "Memory usage is {{ $value }}% for {{ $labels.instance }}."
```

### Test Configurations

#### tests/health-check.yaml
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: microservice-health-check
  labels:
    app.kubernetes.io/name: microservice-template
    app.kubernetes.io/component: test
spec:
  restartPolicy: Never
  containers:
  - name: health-check
    image: curlimages/curl:latest
    command:
    - /bin/sh
    - -c
    - |
      set -e
      echo "Starting health check..."
      
      # Check service discovery
      nslookup microservice-service
      
      # Check health endpoint
      curl -f http://microservice-service/health
      
      # Check readiness endpoint  
      curl -f http://microservice-service/ready
      
      # Check metrics endpoint
      curl -f http://microservice-service:9090/metrics
      
      echo "All health checks passed!"
```

#### tests/integration-test.yaml
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: microservice-integration-test
  labels:
    app.kubernetes.io/name: microservice-template
    app.kubernetes.io/component: test
spec:
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: integration-test
        image: microservice-test:latest
        env:
        - name: SERVICE_URL
          value: "http://microservice-service"
        - name: TEST_SUITE
          value: "integration"
        command:
        - /bin/sh
        - -c
        - |
          set -e
          echo "Running integration tests..."
          
          # Test API endpoints
          curl -f ${SERVICE_URL}/api/v1/users
          curl -f ${SERVICE_URL}/api/v1/health
          
          # Test database connectivity
          curl -f ${SERVICE_URL}/api/v1/status/database
          
          # Test external service integration
          curl -f ${SERVICE_URL}/api/v1/status/external
          
          echo "Integration tests completed successfully!"
  backoffLimit: 3
```

---

## 2. WEB APPLICATION TEMPLATE

### Directory Structure
```
k8s/apps/web-application-template/
├── base/
│   ├── kustomization.yaml
│   ├── frontend-deployment.yaml
│   ├── backend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── backend-service.yaml
│   ├── configmap.yaml
│   └── ingress.yaml
├── overlays/
│   ├── development/
│   ├── staging/
│   └── production/
├── configs/
├── secrets/
├── policies/
├── tests/
├── monitoring/
└── docs/
```

#### base/frontend-deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: frontend-deployment
  labels:
    app.kubernetes.io/name: web-application-template
    app.kubernetes.io/component: frontend
    app.kubernetes.io/part-of: web-platform
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app.kubernetes.io/name: web-application-template
      app.kubernetes.io/component: frontend
  template:
    metadata:
      labels:
        app.kubernetes.io/name: web-application-template
        app.kubernetes.io/component: frontend
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 101  # nginx user
        runAsGroup: 101
        fsGroup: 101
      containers:
      - name: frontend
        image: nginx:alpine
        ports:
        - name: http
          containerPort: 80
          protocol: TCP
        resources:
          requests:
            memory: "32Mi"
            cpu: "10m"
          limits:
            memory: "64Mi"
            cpu: "50m"
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          runAsNonRoot: true
          capabilities:
            drop:
            - ALL
        livenessProbe:
          httpGet:
            path: /
            port: http
          initialDelaySeconds: 10
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /
            port: http
          initialDelaySeconds: 5
          periodSeconds: 5
        volumeMounts:
        - name: nginx-config
          mountPath: /etc/nginx/nginx.conf
          subPath: nginx.conf
        - name: static-content
          mountPath: /usr/share/nginx/html
        - name: tmp
          mountPath: /tmp
        - name: var-cache
          mountPath: /var/cache/nginx
        - name: var-run
          mountPath: /var/run
      volumes:
      - name: nginx-config
        configMap:
          name: frontend-config
      - name: static-content
        configMap:
          name: static-content
      - name: tmp
        emptyDir: {}
      - name: var-cache
        emptyDir: {}
      - name: var-run
        emptyDir: {}
```

---

## 3. DATABASE SERVICE TEMPLATE

#### base/statefulset.yaml
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: database-statefulset
  labels:
    app.kubernetes.io/name: database-template
    app.kubernetes.io/component: database
    app.kubernetes.io/part-of: data-platform
spec:
  serviceName: database-headless
  replicas: 3
  updateStrategy:
    type: RollingUpdate
  selector:
    matchLabels:
      app.kubernetes.io/name: database-template
      app.kubernetes.io/component: database
  template:
    metadata:
      labels:
        app.kubernetes.io/name: database-template
        app.kubernetes.io/component: database
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 999  # postgres user
        runAsGroup: 999
        fsGroup: 999
      containers:
      - name: database
        image: postgres:15-alpine
        ports:
        - name: postgres
          containerPort: 5432
          protocol: TCP
        env:
        - name: POSTGRES_DB
          valueFrom:
            configMapKeyRef:
              name: database-config
              key: database-name
        - name: POSTGRES_USER
          valueFrom:
            secretKeyRef:
              name: database-secrets
              key: username
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: database-secrets
              key: password
        - name: PGDATA
          value: /var/lib/postgresql/data/pgdata
        resources:
          requests:
            memory: "256Mi"
            cpu: "100m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: false  # PostgreSQL needs write access to data directory
          runAsNonRoot: true
          capabilities:
            drop:
            - ALL
        livenessProbe:
          exec:
            command:
            - /bin/sh
            - -c
            - exec pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB" -h 127.0.0.1 -p 5432
          initialDelaySeconds: 30
          periodSeconds: 10
          timeoutSeconds: 5
          successThreshold: 1
          failureThreshold: 6
        readinessProbe:
          exec:
            command:
            - /bin/sh
            - -c
            - exec pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB" -h 127.0.0.1 -p 5432
          initialDelaySeconds: 5
          periodSeconds: 10
          timeoutSeconds: 5
          successThreshold: 1
          failureThreshold: 3
        volumeMounts:
        - name: database-storage
          mountPath: /var/lib/postgresql/data
        - name: database-config
          mountPath: /etc/postgresql/postgresql.conf
          subPath: postgresql.conf
      volumes:
      - name: database-config
        configMap:
          name: database-config
  volumeClaimTemplates:
  - metadata:
      name: database-storage
      labels:
        app.kubernetes.io/name: database-template
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: fast-ssd
      resources:
        requests:
          storage: 100Gi
```

---

## Platform-Specific Configurations

### AWS EKS Platform Templates

#### platforms/aws/storage-class.yaml
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
  annotations:
    storageclass.kubernetes.io/is-default-class: "false"
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
  iops: "3000"
  throughput: "125"
  encrypted: "true"
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
reclaimPolicy: Retain
```

#### platforms/aws/load-balancer.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
  name: microservice-service-nlb
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
    service.beta.kubernetes.io/aws-load-balancer-cross-zone-load-balancing-enabled: "true"
    service.beta.kubernetes.io/aws-load-balancer-backend-protocol: "tcp"
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-protocol: "http"
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-path: "/health"
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-healthy-threshold: "2"
    service.beta.kubernetes.io/aws-load-balancer-healthcheck-unhealthy-threshold: "2"
spec:
  type: LoadBalancer
  selector:
    app.kubernetes.io/name: microservice-template
  ports:
  - name: http
    port: 80
    targetPort: 8080
    protocol: TCP
```

### Azure AKS Platform Templates

#### platforms/azure/storage-class.yaml
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: disk.csi.azure.com
parameters:
  skuName: Premium_LRS
  cachingmode: ReadOnly
  kind: Managed
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
reclaimPolicy: Retain
```

### GCP GKE Platform Templates

#### platforms/gcp/storage-class.yaml
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-ssd
provisioner: pd.csi.storage.gke.io
parameters:
  type: pd-ssd
  replication-type: regional-pd
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
reclaimPolicy: Retain
```

---

## GitOps Templates

### ArgoCD Application Templates

#### gitops/argocd/applications/microservice-app.yaml
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: microservice-template
  namespace: argocd
  labels:
    app.kubernetes.io/name: microservice-template
  finalizers:
    - resources-finalizer.argocd.argoproj.io
spec:
  project: default
  source:
    repoURL: https://github.com/company/k8s-deployments
    targetRevision: HEAD
    path: k8s/apps/microservice-template/overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
      allowEmpty: false
    syncOptions:
    - CreateNamespace=true
    - PrunePropagationPolicy=foreground
    - PruneLast=true
    retry:
      limit: 5
      backoff:
        duration: 5s
        factor: 2
        maxDuration: 3m
  revisionHistoryLimit: 10
```

### ApplicationSet for Multi-Environment

#### gitops/argocd/applicationsets/microservice-environments.yaml
```yaml
apiVersion: argoproj.io/v1alpha1
kind: ApplicationSet
metadata:
  name: microservice-environments
  namespace: argocd
spec:
  generators:
  - list:
      elements:
      - cluster: dev
        url: https://kubernetes.default.svc
        environment: development
        namespace: development
      - cluster: staging
        url: https://kubernetes.default.svc
        environment: staging
        namespace: staging
      - cluster: prod
        url: https://kubernetes.default.svc
        environment: production
        namespace: production
  template:
    metadata:
      name: 'microservice-{{environment}}'
      labels:
        environment: '{{environment}}'
    spec:
      project: default
      source:
        repoURL: https://github.com/company/k8s-deployments
        targetRevision: HEAD
        path: 'k8s/apps/microservice-template/overlays/{{environment}}'
      destination:
        server: '{{url}}'
        namespace: '{{namespace}}'
      syncPolicy:
        automated:
          prune: true
          selfHeal: true
        syncOptions:
        - CreateNamespace=true
```

---

## CI/CD Pipeline Templates

### GitHub Actions Template

#### ci/github-actions/deploy-microservice.yml
```yaml
name: Deploy Microservice

on:
  push:
    branches:
    - main
    - develop
    paths:
    - 'k8s/apps/microservice-template/**'
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deployment environment'
        required: true
        default: 'development'
        type: choice
        options:
        - development
        - staging
        - production

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: microservice-template

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write
    
    outputs:
      image-digest: ${{ steps.build.outputs.digest }}
      image-tag: ${{ steps.meta.outputs.tags }}
    
    steps:
    - name: Checkout
      uses: actions/checkout@v4
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v3
    
    - name: Login to Container Registry
      uses: docker/login-action@v3
      with:
        registry: ${{ env.REGISTRY }}
        username: ${{ github.actor }}
        password: ${{ secrets.GITHUB_TOKEN }}
    
    - name: Extract metadata
      id: meta
      uses: docker/metadata-action@v5
      with:
        images: ${{ env.REGISTRY }}/${{ github.repository }}/${{ env.IMAGE_NAME }}
        tags: |
          type=ref,event=branch
          type=ref,event=pr
          type=sha,prefix={{branch}}-
          type=raw,value=latest,enable={{is_default_branch}}
    
    - name: Build and push
      id: build
      uses: docker/build-push-action@v5
      with:
        context: .
        platforms: linux/amd64,linux/arm64
        push: true
        tags: ${{ steps.meta.outputs.tags }}
        labels: ${{ steps.meta.outputs.labels }}
        cache-from: type=gha
        cache-to: type=gha,mode=max
  
  security-scan:
    needs: build-and-push
    runs-on: ubuntu-latest
    steps:
    - name: Run Trivy vulnerability scanner
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: ${{ needs.build-and-push.outputs.image-tag }}
        format: 'sarif'
        output: 'trivy-results.sarif'
    
    - name: Upload Trivy scan results
      uses: github/codeql-action/upload-sarif@v3
      with:
        sarif_file: 'trivy-results.sarif'

  deploy:
    needs: [build-and-push, security-scan]
    runs-on: ubuntu-latest
    environment: ${{ github.event.inputs.environment || 'development' }}
    
    steps:
    - name: Checkout
      uses: actions/checkout@v4
    
    - name: Configure kubectl
      uses: azure/setup-kubectl@v3
      with:
        version: 'v1.28.0'
    
    - name: Configure kubeconfig
      run: |
        mkdir -p ~/.kube
        echo "${{ secrets.KUBECONFIG }}" | base64 -d > ~/.kube/config
        chmod 600 ~/.kube/config
    
    - name: Update image in Kustomization
      run: |
        cd k8s/apps/microservice-template/overlays/${{ github.event.inputs.environment || 'development' }}
        kustomize edit set image ${{ env.IMAGE_NAME }}=${{ needs.build-and-push.outputs.image-tag }}
    
    - name: Deploy to Kubernetes
      run: |
        kubectl apply -k k8s/apps/microservice-template/overlays/${{ github.event.inputs.environment || 'development' }}
        kubectl rollout status deployment/microservice-deployment -n ${{ github.event.inputs.environment || 'development' }}
    
    - name: Verify deployment
      run: |
        kubectl get pods -l app.kubernetes.io/name=microservice-template -n ${{ github.event.inputs.environment || 'development' }}
        kubectl get services -l app.kubernetes.io/name=microservice-template -n ${{ github.event.inputs.environment || 'development' }}
```

---

## Usage Instructions

### 1. Creating a New Microservice Deployment

```bash
# Copy the microservice template
cp -r k8s/apps/microservice-template k8s/apps/my-new-service

# Update the template files
sed -i 's/microservice-template/my-new-service/g' k8s/apps/my-new-service/**/*.yaml

# Customize for your specific needs
# Edit base/deployment.yaml, base/service.yaml, etc.

# Deploy to development
kubectl apply -k k8s/apps/my-new-service/overlays/development
```

### 2. Platform-Specific Deployment

```bash
# AWS EKS deployment
kubectl apply -f platforms/aws/storage-class.yaml
kubectl apply -k k8s/apps/my-service/overlays/production

# Azure AKS deployment
kubectl apply -f platforms/azure/storage-class.yaml
kubectl apply -k k8s/apps/my-service/overlays/production

# GCP GKE deployment
kubectl apply -f platforms/gcp/storage-class.yaml
kubectl apply -k k8s/apps/my-service/overlays/production
```

### 3. GitOps Deployment

```bash
# Apply ArgoCD application
kubectl apply -f gitops/argocd/applications/my-service-app.yaml

# Or use ApplicationSet for multi-environment
kubectl apply -f gitops/argocd/applicationsets/my-service-environments.yaml
```

## Validation Commands

```bash
# Validate Kubernetes manifests
kubeval k8s/apps/*/base/*.yaml
kubeval k8s/apps/*/overlays/*/*.yaml

# Validate Kustomize configurations
kustomize build k8s/apps/microservice-template/overlays/development --dry-run

# Security validation with Conftest
conftest verify --policy security-policies/ k8s/apps/*/base/*.yaml

# Test deployment
kubectl apply -k k8s/apps/microservice-template/overlays/development --dry-run=server
```

---

**ENFORCEMENT:** These templates are MANDATORY and provide the foundation for all Kubernetes deployments. They follow KISS principles, implement security best practices, and ensure universal platform compatibility. All applications MUST use these templates as starting points and customize them according to specific requirements while maintaining the core structure and security standards.